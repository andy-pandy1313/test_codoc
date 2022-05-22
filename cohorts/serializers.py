from django.contrib.auth.models import User
from rest_framework import serializers

from cohorts.models import Cohort, Comment
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


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset = User.objects.all())
    patient = serializers.PrimaryKeyRelatedField(queryset = Patient.objects.all())
    cohort = serializers.PrimaryKeyRelatedField(queryset = Cohort.objects.all())

    class Meta:
        model = Comment
        fields = ('id', 'comment', 'owner', 'cohort', 'patient', 'created_at', 'updated_at')
