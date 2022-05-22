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
    

    '''
    Question 2 : Add model Comments, I've added a factory, url and ModelViewSet too, inspired by the Cohorts factory, view and url.
    '''

class Comment(models.Model):
    comment = models.CharField(max_length=500)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
