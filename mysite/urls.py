from django.urls import path
from . import views

urlpatterns = [
path("",views.index, name="index"),
path("mentorship", views.mentorship, name = "mentorship"),
path("consultation", views.consultation, name = "consultation"),

]
