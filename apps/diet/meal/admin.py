from django.contrib import admin

from apps.diet.meal.models import Meal
from apps.diet.food_options.models import FoodOptions
from apps.diet.meal_general_info.models import MealGeneralInfo


class MealGeneralInfoInline(admin.TabularInline):
    model = MealGeneralInfo


class FoodOptionsInline(admin.TabularInline):
    model = FoodOptions


class MealAdmin(admin.ModelAdmin):
    list_display = ['id', 'diet']
    inlines = [MealGeneralInfoInline, FoodOptionsInline]


admin.site.register(Meal, MealAdmin)
