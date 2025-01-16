from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from blog.views import PostViewSet
from portfolio.views import ProjectViewSet
from resume.views import EducationViewSet, WorkExperienceViewSet, SkillViewSet, CertificationViewSet
from home.views import HomeViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'education', EducationViewSet)
router.register(r'experience', WorkExperienceViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'certifications', CertificationViewSet)
router.register(r'home', HomeViewSet, basename='home')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]