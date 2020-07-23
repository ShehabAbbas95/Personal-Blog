from django.db import models

# Create your models here.
class info(models.Model):
    name = models.CharField(max_length= 64)
    age = models.CharField(max_length= 64)
    email = models.CharField(max_length= 64)
    phone = models.CharField(max_length= 64)
    highest_education = models.CharField(max_length= 64)
    level= models.CharField(max_length= 64)
    track = models.CharField(max_length= 64)
    describtion = models.CharField(max_length= 64,null = True)
