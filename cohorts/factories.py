import factory

from cohorts.models import Cohort
from commons.factories import UserFactory


class CohortFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('word')
    description = factory.Faker('text')
    owner = factory.SubFactory(UserFactory)

    class Meta:
        model = Cohort
