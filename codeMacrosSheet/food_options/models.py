from django.db import models
from meal.models import Meal
from django.core.validators import MinValueValidator


class UnitOfMeasurement(models.TextChoices):
    G = 'g', 'g'
    U = 'U', 'U'
    ML = 'ml', 'ml'


class FoodOptions(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, default=None)
    food = models.CharField(max_length=100) 
    quantity =  models.FloatField(default=1, validators=[MinValueValidator(1)])
    unit_of_measurement = models.CharField(max_length=50, choices=UnitOfMeasurement.choices)