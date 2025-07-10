from django.db import models
from django.contrib.auth.models import AbstractUser


class Traveler(AbstractUser):
    favorite_routs = models.ManyToManyField(
        "journeys.Route",
        related_name="liked_by",
        blank=True
    )
