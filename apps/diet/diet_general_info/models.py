from django.db import models
from django.core.validators import MinValueValidator

from apps.diet.diet.models import Diet


class TypeOfDiet(models.TextChoices):
    MAINTENANCE = 'Maintenance', 'Maintenance'
    BULKING = 'Bulking', 'Bulking'
    CUTTING = 'Cutting', 'Cutting'


class DietGeneralInfo(models.Model):
    diet = models.OneToOneField(Diet, on_delete=models.CASCADE, default=None)
    goal = models.CharField(max_length=100, blank=True)
    observations = models.CharField(max_length=300, blank=True)
    initial_date = models.DateField()
    final_date = models.DateField()
    weeks = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    type_of_diet = models.CharField(max_length=50, choices=TypeOfDiet.choices, default=TypeOfDiet.MAINTENANCE )
    
    

