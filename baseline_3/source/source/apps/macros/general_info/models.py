from django.db import models
from django.core.validators import MinValueValidator
from apps.macros.macros_planner.models import MacrosPlanner

class GeneralInfo(models.Model):
    macros_planner = models.OneToOneField(MacrosPlanner, on_delete=models.CASCADE, default=None)
    goal = models.CharField(max_length=100, blank=True)
    initial_date = models.DateField()
    final_date = models.DateField()
    weeks = models.IntegerField(default=1, validators=[MinValueValidator(1)])

   

