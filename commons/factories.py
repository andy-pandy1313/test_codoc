import factory
from django.contrib.auth.models import User


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker('word')

    class Meta:
        model = User
