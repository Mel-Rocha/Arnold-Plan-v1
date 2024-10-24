from django.contrib import admin

from apps.diet.food_options.models import FoodOptions


class FoodOptionsAdmin(admin.ModelAdmin):
    list_display = ('food', 'quantity', 'unit_of_measurement')


admin.site.register(FoodOptions, FoodOptionsAdmin)
