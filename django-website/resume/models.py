from django.db import models

class Education(models.Model):
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    field_of_study = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.degree} in {self.field_of_study} from {self.institution}"


class WorkExperience(models.Model):
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    responsibilities = models.TextField()

    def __str__(self):
        return f"{self.position} at {self.company}"


class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Certification(models.Model):
    title = models.CharField(max_length=255)
    issued_by = models.CharField(max_length=255)
    date_issued = models.DateField()

    def __str__(self):
        return self.title