from django.shortcuts import render
from django.utils import timezone
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from .models import *
from mysite.models import info
from django.http import HttpResponse, JsonResponse
import json
# Create your views here.

def index(request):
        if request.is_ajax():
            z = list(Post.objects.order_by('published_date').values())
            new_title = {"title": z[-1]["post_heading"],
                "text": z[-1]["post_text"],
                "id": z[-1]["id"],}

            return JsonResponse((new_title) ,safe=False)
        else:
            posts = list(Post.objects.order_by('published_date').values())
            last_post = {"title":posts[-1]["post_heading"],
               "text": posts[-1]["post_text"],}
            return render(request, 'blog/index.html', {"posts":posts,"last_post":last_post})


def likePost(request):
        if request.method == 'GET':
               post_id = request.GET['post_id']
               likedpost = Post.objects.get(pk=post_id) #getting the liked posts
               m = Like(post=likedpost) # Creating Like Object
               m.save()  # saving it to store in database
               return HttpResponse("Success!") # Sending an success response
        else:
               return HttpResponse("Request method is not a GET")
