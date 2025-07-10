from django.db import models
from django.contrib.auth.models import AbstractUser


class Traveler(AbstractUser):
    favorite_routs = models.ManyToManyField(
        "journey.Routes",
        related_name="liked_by",
        blank=True
    )
