from django.urls import path
from . import views
from django.conf.urls.static import static
from blog import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:post_id>', views.posts, name='posts'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
