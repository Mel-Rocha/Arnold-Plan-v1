from django.db import models
from enum import Enum, auto

class KcalLevel(Enum):
    is_low_kcal = auto()
    is_normal_kcal = auto()
    is_high_kcal = auto()

class MacrosSheet(models.Model):
    cho = models.FloatField(default=0)
    ptn = models.FloatField(default=0)
    fat = models.FloatField(default=0)
    kcal = models.FloatField(default=0)
    kcal_level = models.CharField(max_length=20, default=KcalLevel.is_normal_kcal.name)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.calculate_kcal_level()

    def calculate_kcal_level(self):
        self.kcal = (self.cho * 4) + (self.ptn * 4) + (self.fat * 9)

    def calculate_kcal_level(self):
        self.kcal = (self.cho * 4) + (self.ptn * 4) + (self.fat * 9)

        if self.kcal < 1500:
            self.kcal_level = KcalLevel.is_low_kcal.name
        elif self.kcal > 2000:
            self.kcal_level = KcalLevel.is_high_kcal.name
        else:
            self.kcal_level = KcalLevel.is_normal_kcal.name

    def save(self, *args, **kwargs):
        self.calculate_kcal_level()
        super().save(*args, **kwargs)




