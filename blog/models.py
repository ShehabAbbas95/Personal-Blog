from django.db import models
from multiselectfield import MultiSelectField
class Categoreies(models.Model):
    category_name = models.CharField(max_length=200)
    def __str__(self):
        return self.category_name

class Post(models.Model):
            post_heading = models.CharField(max_length=200)
            post_text = models.TextField()
            published_date = models.DateTimeField(auto_now=True)
            id = models.AutoField(primary_key=True)
            image = models.ImageField(upload_to='images/',blank=True)
            category = models.ManyToManyField(Categoreies,blank=True)
            def __str__(self):
                 return (self.post_heading)
class React(models.Model):
        post_id = models.IntegerField()
        no_of_likes = models.IntegerField(default=0)
        no_of_dislikes = models.IntegerField(default=0)

class Userscomment(models.Model):
    comment= models.CharField(max_length=512)
    username= models.CharField(max_length=200)
    published_date = models.DateTimeField(auto_now=True)
    post_id = models.IntegerField()
    user_id = models.AutoField(primary_key=True)
