from django.db import models
from django.core.validators import MinValueValidator

class GeneralInfo(models.Model):
    goal = models.CharField(max_length=100, blank=True)
    initial_date = models.DateField()
    final_date = models.DateField()
    weeks = models.IntegerField(default=1, validators=[MinValueValidator(1)])

   

