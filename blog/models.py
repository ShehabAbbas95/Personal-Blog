from django.db import models

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length = 265)
    text = models.TextField()
    class Media:
        js = (
            '//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js', # jquery
            'blog/js/myscript.js',   # app static folder
        )
        css = {
        'all': ('blog/css/admin/styles.css',)
         }
