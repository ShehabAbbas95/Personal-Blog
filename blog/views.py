from django.shortcuts import render
from .models import *
from django.http import Http404, HttpResponse
# Create your views here.

def blog_home(request):

        return render(request, "blog/try.html")


def x(request):
    if request.is_ajax():
    #    currency = requesst.POST.get("currency")
    #    res = request.get("https://api.exchangeratesapi.io/latest", params = {
    #    "base":"USD", "symbols":currency
    #    })
    #    return JsonResponse(res)
        li = ["asda","adsdasdasdad"]
        data = json(li)
        return HttpResponse(data, content_type='application/json')
    else:
        raise Http404
