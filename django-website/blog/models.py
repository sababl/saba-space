from django.db import models
from mysite.models import BaseModel
from portfolio.models import Category
class Post(BaseModel):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category)
    def __str__(self):
        return self.title