from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class Gender(models.TextChoices):
    MALE = 'Male', 'Male'
    FEMALE = 'Female', 'Female'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    birth_date = models.DateField()
    weight = models.FloatField(default=1, validators=[MinValueValidator(1)])
    height = models.FloatField(default=1, validators=[MinValueValidator(1)])
    gender = models.CharField(max_length=50, choices=Gender.choices)

    def __str__(self):
        return self.user.username
