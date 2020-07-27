from django.conf.urls import url
from . import views
urlpatterns = [
        url('', views.index, name='index'),  # index view at /
        url(r'^likepost/$', views.likePost, name='likepost'),
   ]
