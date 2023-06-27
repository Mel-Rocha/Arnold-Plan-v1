from django.db import models
from kcal.models import calculate_kcal, calculate_kcal_level 
from kcal.models import KcalLevel

class MacrosSheet(models.Model):
    cho = models.FloatField(default=0)
    ptn = models.FloatField(default=0)
    fat = models.FloatField(default=0)
    kcal = models.FloatField(default=0)
    kcal_level = models.CharField(max_length=20, default=KcalLevel.is_normal_kcal.name)

    def calculate_kcal_and_levels(self):
        self.kcal = calculate_kcal(self.cho, self.ptn, self.fat)
        self.kcal_level = calculate_kcal_level(self.kcal)

    def save(self, *args, **kwargs):
        self.calculate_kcal_and_levels()
        super().save(*args, **kwargs)
