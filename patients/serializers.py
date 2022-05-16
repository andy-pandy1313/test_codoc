from rest_framework import serializers

from patients.models import Patient


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('id', 'last_name', 'first_name', 'birth_date', 'sex', 'residence_country')
