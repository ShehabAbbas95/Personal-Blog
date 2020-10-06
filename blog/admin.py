from django.contrib.admin import AdminSite

from .models import *

class MyAdminSite(AdminSite):
    site_header = 'Monty Python administration'

admin_site = MyAdminSite(name='myadmin')



admin_site.register(Post)
admin_site.register(React)
admin_site.register(Categoreies)
admin_site.register(Userscomment)
