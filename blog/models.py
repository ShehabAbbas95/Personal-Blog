from django.db import models

# Create your models here.
class Post(models.Model):
            post_heading = models.CharField(max_length=200)
            post_text = models.TextField()
            published_date = models.DateTimeField(auto_now_add=True)
            id = models.AutoField(primary_key=True)
            image = models.ImageField(upload_to='images/') 

            def __str__(self):      # If python2 use __str__ if python3
                 return (self.post_heading)
class Like(models.Model):
        post = models.ForeignKey(Post, on_delete = models.CASCADE)
