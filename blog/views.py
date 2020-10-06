from django.shortcuts import render
from django.utils import timezone
from django.db.models import F,Q
from django.core.exceptions import ObjectDoesNotExist
from django.core.serializers.json import DjangoJSONEncoder
from .models import *
from mysite.models import info
from django.urls import reverse
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
import json
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from .forms import *
from django.contrib import messages
# Create your views here.
all_posts = Post.objects.all()
categories = Categoreies.objects.all()
class Posts(ListView):
    model = Post
    template_name = 'blog/index.html' # app//model_viewtype.html
    context_object_name= 'posts'
    ordering = ['-published_date']
    paginate_by = 5
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['categories'] = categories
        return context
# class PostDetailView(DetailView):
#     model = Post
#     def get(self, request, *args, **kwargs):
#         post = get_object_or_404(Post, pk=kwargs['id'])
#         context = {'post': post}
#         return render(request, 'blog/post_detail.html', context)
def detail(request,id):
    post = all_posts.filter(id = id).all()

    try:
        reacts = (React.objects.filter(post_id = id).values())
    except ObjectDoesNotExist:
        reacts = 'Be the First To Like This'
    context = {'post_detail' : post,
            'comments' : Userscomment.objects.filter(post_id = id).order_by('-published_date').all(),
            'post_title': list(post.values())[0]["post_heading"],
            'reacts': reacts,}
    return render(request, 'blog/post-detail.html', context)
def index_ajax(request):
    posts = list(all_posts.order_by('published_date').values())
    new_post = {"title": posts[-1]["post_heading"],
        "text": posts[-1]["post_text"],
        "id": posts[-1]["id"],}
    return JsonResponse((new_post) ,safe=False)
    
def like(request):
    id = request.POST.get('id')
    # these values detrmines which ajax call is going to execute (like or dislike)
    voting = (request.POST.get('voting'))
    color = (request.POST.get('color'))
    post_reacts = React.objects.filter(post_id = id).all()
    if not post_reacts:
        if int(voting) > 0:
            react = React( post_id = id,no_of_likes= 1)
        else:
            react = React( post_id = id,no_of_dislikes=-1)
        react.save()
        users_reacts = {'prev_reacts':post_reacts}
        return HttpResponse('success')
    likes =  list(post_reacts.values())[0]['no_of_likes']
    dislikes = list(post_reacts.values())[0]['no_of_dislikes']
    react = React.objects.get(post_id=id)
    if int(voting) > 0:
        react.no_of_likes = F('no_of_likes') + int(voting)
    if int(voting) < 0 :
        react.no_of_dislikes = F('no_of_dislikes') + int(voting)
    if color == 'blue':
        react.no_of_likes = F('no_of_likes') - 1
    if  color == 'red':
        react.no_of_dislikes = F('no_of_dislikes') + 1
    react.save()
    users_reactions = {'likes':likes,
                   'dislikes':abs(dislikes),
                   'color':color}
    return JsonResponse((users_reactions) ,safe=False)
def search_and_category(request,category=None):
    if category:
        posts= all_posts.filter(category__category_name = category).all()
        if posts:
            categoreies = categories.filter(category_name = category )
            return render(request,'blog/index.html',{'posts':posts,'categories':categoreies})
        else:
             messages.error(request,'No Posts In that category yet')
             return HttpResponseRedirect(reverse('blog'))
    category = request.GET.get('search')
    posts = all_posts.filter(post_heading__icontains = category)
    return render(request,'blog/index.html',{'posts':posts,'categories':categories})
