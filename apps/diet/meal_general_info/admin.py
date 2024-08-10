from django.contrib import admin
from .models import MealGeneralInfo


class MealGeneralInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'time', 'type_of_meal')


admin.site.register(MealGeneralInfo, MealGeneralInfoAdmin)
