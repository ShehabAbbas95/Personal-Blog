from django.shortcuts import render
from django.core import serializers
from .models import Post, Like
from mysite.models import info
from django.http import HttpResponse, JsonResponse

def index(request):
        #posts = Post.objects.all()  # Getting all the posts from database
        #return render(request, 'post/index.html', { 'posts': posts })
        if request.is_ajax():
            y = (Post.objects.values())
            x = Post.objects.latest()


            return JsonResponse(x,y, safe=False)
        else:
            post = Post.objects.values()
            return render(request, 'post/index.html', {"post":post})
def likePost(request):
        if request.method == 'GET':
               post_id = request.GET['post_id']
               likedpost = Post.objects.get(pk=post_id) #getting the liked posts
               m = Like(post=likedpost) # Creating Like Object
               m.save()  # saving it to store in database
               return HttpResponse("Success!") # Sending an success response
        else:
               return HttpResponse("Request method is not a GET")
