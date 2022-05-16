from django.db.models import TextChoices


class Sex(TextChoices):
    M = ("M", "Male")
    F = ("F", "Female")
