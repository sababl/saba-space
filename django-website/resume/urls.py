from django.urls import path
from rest_framework import routers
from .views import EducationViewSet, WorkExperienceViewSet, SkillViewSet, CertificationViewSet

router = routers.DefaultRouter()
router.register(r'education', EducationViewSet)
router.register(r'experience', WorkExperienceViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'certifications', CertificationViewSet)

urlpatterns = router.urls