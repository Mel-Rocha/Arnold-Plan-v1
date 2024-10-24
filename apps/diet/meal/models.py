from django.db import models

from apps.diet.diet.models import Diet


class Meal(models.Model):
    diet = models.ForeignKey(Diet, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"Meal #{self.id}"
