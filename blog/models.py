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
class Userscomment(models.Model):
    comment= models.CharField(max_length=512)
    username= models.CharField(max_length=200)
class Friend(models.Model):
    # NICK NAME should be unique
    nick_name = models.CharField(max_length=100, unique =  True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    likes = models.CharField(max_length = 250)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    lives_in = models.CharField(max_length=150, null = True, blank = True)

    def __str__(self):
        return self.nick_name
