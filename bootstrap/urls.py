from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    path('',views.index, name= "index"),
    path('trys/',views.trys, name="trys"),
    url('try1',views.try1, name= 'try1')

]
