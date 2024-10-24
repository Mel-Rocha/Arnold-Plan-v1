from django.db import models
from django.core.validators import MinValueValidator

from apps.macros.macros_planner.models import MacrosPlanner
from apps.macros.calcs.calcs import KcalLevel, CalcMacroLevel, ProportionGKG


class MacrosSheet(models.Model):
    macros_planner = models.ForeignKey(MacrosPlanner, on_delete=models.CASCADE, default=None)
    week = models.PositiveIntegerField(default=0)
    cho = models.FloatField(default=1, validators=[MinValueValidator(1)])
    ptn = models.FloatField(default=1, validators=[MinValueValidator(1)])
    fat = models.FloatField(default=1, validators=[MinValueValidator(1)])
    kcal = models.FloatField(default=0)

    @property
    def profile(self):
        return self.macros_planner.profile

    @property
    def weight(self):
        return self.profile.weight

    @property
    def kcal_level(self):
        return KcalLevel.calculate_kcal_level(self.kcal)

    @property
    def cho_level(self):
        return CalcMacroLevel().calculate_macro_level(self.cho, self.kcal, 'cho')

    @property
    def ptn_level(self):
        return CalcMacroLevel().calculate_macro_level(self.ptn, self.kcal, 'ptn')

    @property
    def fat_level(self):
        return CalcMacroLevel().calculate_macro_level(self.fat, self.kcal, 'fat')

    @property
    def cho_proportion(self):
        proportions = ProportionGKG(self.weight, self.cho, self.ptn, self.fat)
        return round(proportions.cho_proportion, 2)

    @property
    def ptn_proportion(self):
        proportions = ProportionGKG(self.weight, self.cho, self.ptn, self.fat)
        return round(proportions.ptn_proportion, 2)

    @property
    def fat_proportion(self):
        proportions = ProportionGKG(self.weight, self.cho, self.ptn, self.fat)
        return round(proportions.fat_proportion, 2)

    def update_week_based_on_id(self):
        if self.week == 0 and self.macros_planner:
            original_size = self.macros_planner.macrossheet_set.count()
            print(f'Original: {original_size}')

            macros_sheets = self.macros_planner.macrossheet_set.all().order_by('id')

            for index, macros_sheet in enumerate(macros_sheets):
                macros_sheet.week = index + 1
                macros_sheet.save()

            macros_sheets = self.macros_planner.macrossheet_set.all().order_by('id')
            current_size = macros_sheets.count()
            print(f'Atual: {current_size}')

            if current_size < original_size:
                for index, macros_sheet in enumerate(macros_sheets):
                    macros_sheet.week = index + 1
                    macros_sheet.save()

            self.week = macros_sheets.last().week + 1
            self.macros_planner.save()

    def save(self, *args, **kwargs):
        self.kcal = KcalLevel.calculate_kcal(self.cho, self.ptn, self.fat)
        super().save(*args, **kwargs)
        self.update_week_based_on_id()
