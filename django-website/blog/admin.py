from django.apps import AppConfig
from django.contrib import admin
from .models import Post


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'


admin.site.register(Post)