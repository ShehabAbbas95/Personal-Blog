from django.shortcuts import render
from django.utils import timezone
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
    paginate_by = 3
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
    context = {'post' : Post.objects.filter(id = id).all(),
               'comments' : Userscomment.objects.filter(post_id = id).all()}

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
def likepost(request):
    user_data = Userscomment(comment = request.POST.get('comment'),
                            username = request.POST.get('username'), post_id = request.POST.get('id'))
    user_data.save()
    lastcomment = list(Userscomment.objects.order_by('published_date').values())
    lastcomment = {"comment": lastcomment[-1]["comment"],
        "username": lastcomment[-1]["username"],}
    return JsonResponse((lastcomment) ,safe=False)
