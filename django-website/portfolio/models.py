from django.db import models
from mysite.models import BaseModel

class Post(BaseModel):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, default=title)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Category(BaseModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

class Technology(BaseModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Technologies'


class Project(BaseModel):
    image = models.ImageField(upload_to='images/', blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.ManyToManyField(Technology, related_name='projects')
    github_link = models.URLField()
    slug = models.SlugField(max_length=200, unique=True, default=title)
    demo_link = models.URLField(blank=True)
    category = models.ManyToManyField(
        Category,
        related_name='projects'
    )
    
    def __str__(self):
        return self.title


class Education(BaseModel):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.degree} from {self.institution}"


class WorkExperience(BaseModel):
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.position} at {self.company}"


class Skill(BaseModel):
    name = models.CharField(max_length=100)
    related_projects = models.ManyToManyField(Project, related_name='skills', blank=True)
    def __str__(self):
        return self.name


class Certification(BaseModel):
    title = models.CharField(max_length=200)
    issued_by = models.CharField(max_length=200)
    date_issued = models.DateField()
    image = models.ImageField(upload_to='images/', blank=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title