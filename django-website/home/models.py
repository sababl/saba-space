from django.db import models
from mysite.models import BaseModel

# Create your models here.
class Home(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    about = models.TextField()