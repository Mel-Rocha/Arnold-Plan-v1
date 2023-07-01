from django.db import models
from kcal.enums import KcalLevel
from kcal.enums import calculate_kcal, calculate_kcal_level
from cho.enums import ChoLevel 
from cho.enums import calculate_cho_level
from ptn.enums import PtnLevel
from ptn.enums import calculate_ptn_level
from fat.enums import FatLevel
from fat.enums import calculate_fat_level
from macros_planner.models import MacrosPlanner
from proportion_gkg.calcs import ProportionGKG
from profile_.models import Profile
from django.core.validators import MinValueValidator


class MacrosSheet(models.Model):
    macros_planner = models.ForeignKey(MacrosPlanner, on_delete=models.CASCADE, default=None)
    cho = models.FloatField(default=1, validators=[MinValueValidator(1)])
    ptn = models.FloatField(default=1, validators=[MinValueValidator(1)])
    fat = models.FloatField(default=1, validators=[MinValueValidator(1)])
    kcal = models.FloatField(default=0)
    kcal_level = models.CharField(max_length=20, default=KcalLevel.is_normal_kcal.name)
    cho_level = models.CharField(max_length=20, default=ChoLevel.is_normal_cho.name)
    ptn_level = models.CharField(max_length=20, default=PtnLevel.is_normal_ptn.name)
    fat_level = models.CharField(max_length=20, default=FatLevel.is_normal_fat.name)
    cho_proportion = models.FloatField(default=0)
    ptn_proportion = models.FloatField(default=0)
    fat_proportion = models.FloatField(default=0)

    def calculate_kcal_and_levels(self):
        self.kcal = calculate_kcal(self.cho, self.ptn, self.fat)
        self.kcal_level = calculate_kcal_level(self.kcal)

    def calculate_macros_levels(self):
        self.cho_level = calculate_cho_level(self.cho, self.kcal)
        self.ptn_level = calculate_ptn_level(self.ptn, self.kcal)
        self.fat_level = calculate_fat_level(self.fat, self.kcal)

    
    def calculate_proportions(self):
        
        profile = self.macros_planner.profile
        weight = profile.weight

        proportions = ProportionGKG(weight, self.cho, self.ptn, self.fat)
        self.cho_proportion = round(proportions.cho_proportion, 2)
        self.ptn_proportion = round(proportions.ptn_proportion, 2)
        self.fat_proportion = round(proportions.fat_proportion, 2)
    

    def save(self, *args, **kwargs):
        self.calculate_kcal_and_levels()
        self.calculate_macros_levels()
        self.calculate_proportions()
        super().save(*args, **kwargs)