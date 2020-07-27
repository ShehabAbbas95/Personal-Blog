from django.contrib import admin
from .models import *
from django.conf.urls import url
# Register your models here.


admin.site.site_header = 'Website admin'
admin.site.site_title = 'Website admin'

admin.site.index_title = 'Website administration'
admin.empty_value_display = '**Empty**'

admin.site.register(Like)
class MyModelAdmin(admin.ModelAdmin):
    admin.site.register(Post)

    class Media:
        css = {
            "all": ("css/style.css",)
        }
        js = ("js/myscript.js",)
