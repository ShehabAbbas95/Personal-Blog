from django.shortcuts import render
from django.utils import timezone
from django.db.models import F
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from .models import *
from mysite.models import info
from django.http import HttpResponse, JsonResponse
import json
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from .forms import *
# Create your views here.

class Posts(ListView):
    model = Post
    template_name = 'blog/index.html' # app//model_viewtype.html
    context_object_name= 'posts'
    ordering = ['-published_date']
    paginate_by = 5
    # def get_context_data(self, **kwargs):
    #     context = super(Posts, self).get_context_data(**kwargs)
    #     context['form'] = NameForm()
        # Add any other variables to the context here
        # return context
class PostDetailView(DetailView):
    model = Post
    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['id'])
        context = {'post': post}
        return render(request, 'blog/post_detail.html', context)
def detail(request,id):
    post = Post.objects.filter(id = id).all()
    for x in post:
        y = (json.dumps(x.categorey))


    try:
        reacts = (React.objects.filter(post_id = id).values())
    except ObjectDoesNotExist:
        reacts = 'Be the First To Like This'
    context = {'post' : post,
            'comments' : Userscomment.objects.filter(post_id = id).order_by('-published_date').all(),
            'post_title': list(post.values())[0]["post_heading"],
            'reacts': (reacts),
            'post_categoreies':y}
    return render(request, 'blog/post-detail.html', context)

# def likePost(request):
#         if request.method == 'GET':
#                post_id = request.GET['post_id']
#                likedpost = Post.objects.get(pk=post_id) #getting the liked posts
#                m = Like(post=likedpost) # Creating Like Object
#                m.save()  # saving it to store in database
#                return HttpResponse("Success!") # Sending an success response
#         else:
#                return HttpResponse("Request method is not a GET")
def index_ajax(request):
    posts = list(Post.objects.order_by('published_date').values())
    new_post = {"title": posts[-1]["post_heading"],
        "text": posts[-1]["post_text"],
        "id": posts[-1]["id"],}

    return JsonResponse((new_post) ,safe=False)
# def likepost(request):
#          userinfo= Userscomment()
#          userinfo.comment= request.POST.get('firstnamevalue')
#          userinfo.username= request.POST.get('lastnamevalue')
#          userinfo.save()
#          return HttpResponse("Success")
def comment(request):
    user_data = Userscomment(comment = request.POST.get('comment'),
                            username = request.POST.get('username'), post_id = request.POST.get('id'))
    user_data.save()
    lastcomment = list(Userscomment.objects.order_by('published_date').values())
    lastcomment = {"comment": lastcomment[-1]["comment"],
        "username": lastcomment[-1]["username"],}
    return JsonResponse((lastcomment) ,safe=False)
def like(request):
    id = request.POST.get('id')
    # these values detrmines which ajax call is going tor execut (like or dislike)
    voting = (request.POST.get('voting'))
    color = (request.POST.get('color'))
    post_reacts = React.objects.filter(post_id = id).all()
    if not post_reacts:
        if int(voting) > 0:
            react = React( post_id = id,no_of_likes= 1)
        else:
            react = React( post_id = id,no_of_dislikes=-1)
        react.save()
        users_reacts = {'prev_reacts':React.objects.filter(post_id = id).all()}
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
