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
# Create your views here.

class Posts(ListView):
    model = Post
    template_name = 'blog/index.html' # app//model_viewtype.html
    context_object_name= 'posts'
    ordering = ['-published_date']
    paginate_by = 3
class PostDetailView(DetailView):
    model = Post
    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['id'])
        context = {'post': post}
        return render(request, 'blog/post_detail.html', context)
def detail(request,id):
    post = Post.objects.filter(id = id).all()
    return render(request, 'blog/post-detail.html', {"post":post})
def likePost(request):
        if request.method == 'GET':
               post_id = request.GET['post_id']
               likedpost = Post.objects.get(pk=post_id) #getting the liked posts
               m = Like(post=likedpost) # Creating Like Object
               m.save()  # saving it to store in database
               return HttpResponse("Success!") # Sending an success response
        else:
               return HttpResponse("Request method is not a GET")
def index_ajax(request):
    posts = list(Post.objects.order_by('published_date').values())
    new_post = {"title": posts[-1]["post_heading"],
        "text": posts[-1]["post_text"],
        "id": posts[-1]["id"],}

    return JsonResponse((new_post) ,safe=False)
