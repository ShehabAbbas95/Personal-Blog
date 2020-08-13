from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
        path('post/', views.index, name='index'),  # index view at /
        url(r'^likepost/$', views.likePost, name='likepost'),

   ]
