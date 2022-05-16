from django.contrib.auth.models import User
from django.db import models

from patients.models import Patient


class Cohort(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    patients = models.ManyToManyField(Patient, related_name="cohorts")
