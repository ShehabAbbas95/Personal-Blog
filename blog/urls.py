from django.urls import path
from django.conf.urls import url
from . import views
from .views import Posts, PostDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("blog/",Posts.as_view(), name="blog"),
    path("blog/post/<int:id>/",views.detail, name="detail"),
    path('blog/index_ajax',views.index_ajax,name='index_ajax')
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
