from django.conf.urls import url
from . import views
urlpatterns = [
        url('', views.index, name='index'),  # index view at /
        url(r'^likepost/$', views.likePost, name='likepost'),
        url('index', views.index, name='index')  # likepost view at /likepost
   ]
