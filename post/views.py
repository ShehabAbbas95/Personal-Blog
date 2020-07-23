from django.shortcuts import render
from django.core import serializers
from .models import Post, Like
from django.http import HttpResponse, JsonResponse

def index(request):
        #posts = Post.objects.all()  # Getting all the posts from database
        #return render(request, 'post/index.html', { 'posts': posts })
        if request.is_ajax():
            x = serializers.serialize('json',(Post.objects.all()))
            return JsonResponse(x, content_type="application/json", safe=False)
        else:
            post = Post.objects.all()
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
