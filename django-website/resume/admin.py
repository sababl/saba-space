from django.contrib import admin
from .models import Education, WorkExperience, Skill, Certification

admin.site.register(Education)
admin.site.register(WorkExperience)
admin.site.register(Skill)
admin.site.register(Certification)