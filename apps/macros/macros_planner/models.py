from django.db import models

from apps.user.profile_.models import Profile


class MacrosPlanner(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"MacrosPlanner #{self.id}"
