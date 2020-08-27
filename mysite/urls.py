from django.urls import path
from . import views

urlpatterns = [
path("",views.index, name="home"),
path("mentorship", views.mentorship, name = "mentorship"),
path("consultation", views.consultation, name = "consultation"),

]
