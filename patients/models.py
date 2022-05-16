from django.db import models
from patients.enums import Sex

class Patient(models.Model):
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    sex = models.CharField(max_length=1, choices=Sex.choices)
    residence_country = models.CharField(max_length=255, null=True, default=None)
