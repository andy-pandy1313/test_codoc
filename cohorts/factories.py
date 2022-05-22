import factory

from cohorts.models import Cohort
from cohorts.models import Comment
from commons.factories import UserFactory
from patients.factories import PatientFactory

class CohortFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('word')
    description = factory.Faker('text')
    owner = factory.SubFactory(UserFactory)

    class Meta:
        model = Cohort

class CommentsFactory(factory.django.DjangoModelFactory):
    comment = factory.Faker('text')
    owner = factory.SubFactory(UserFactory)
    patient = factory.SubFactory(PatientFactory)
    cohort = factory.SubFactory(CohortFactory)

    class Meta:
        model = Comment
