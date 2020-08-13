from django.shortcuts import render
from post.models import *
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
    return render(request, "bootstrap/navbar.html")


def trys(request):
    if request.is_ajax():
        z = list(Post.objects.values())
        x = {"title": z[-1]["post_heading"],
            "text": z[-1]["post_text"],}
        return JsonResponse((x) ,safe=False)
    else:
        return render(request, 'bootstrap/try.html')

@csrf_exempt
def try1(request):
    if request.method == 'POST':
        #x = {"text":"ahmed"}
        z = request.POST.get('ok')
        return JsonResponse((z) ,safe=False)

    else:

        post = Post.objects.values()
        return render(request, 'bootstrap/try1.html', {"post":post})
