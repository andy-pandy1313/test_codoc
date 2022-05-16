from datetime import timedelta
from random import randint

import factory.fuzzy
from django.utils import timezone
from patients.enums import Sex
from patients.models import Patient


class PatientFactory(factory.django.DjangoModelFactory):
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    birth_date = (timezone.now() - timedelta(weeks=randint(0, 4000))).replace(hour=0, minute=0, second=0, microsecond=0)
    sex = factory.fuzzy.FuzzyChoice(Sex)
    residence_country = factory.Faker('country')

    class Meta:
        model = Patient
