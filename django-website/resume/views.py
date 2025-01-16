from rest_framework import viewsets
from rest_framework.response import Response
from .models import Education, WorkExperience, Skill, Certification
from .serializers import (
    EducationSerializer, 
    WorkExperienceSerializer,
    SkillSerializer,
    CertificationSerializer
)

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class WorkExperienceViewSet(viewsets.ModelViewSet):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class CertificationViewSet(viewsets.ModelViewSet):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer
