from django.contrib.auth.models import User
from rest_framework import serializers

from cohorts.models import Cohort
from patients.models import Patient
from patients.serializers import PatientSerializer


class CohortSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    patients = PatientSerializer(read_only=True, many=True)
    patient_ids = serializers.PrimaryKeyRelatedField(
        write_only=True, many=True, required=False, source="patients", queryset=Patient.objects.all()
    )

    class Meta:
        model = Cohort
        fields = (
            'id', 'name', 'description', 'owner', 'created_at', 'updated_at',
            # read-only
            'patients',
            # write-only
            'patient_ids',
        )
