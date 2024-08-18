from django.contrib import admin
from apps.user.models import Athlete, Nutritionist


class AthleteAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'category', 'weight', 'height', 'birth_date', 'is_pro')
    search_fields = ('name', 'category', 'user__username')
    list_filter = ('category', 'is_pro')

class NutritionistAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'crn', 'academic_degree', 'area_of_specialization')
    search_fields = ('name', 'crn', 'user__username')
    list_filter = ('academic_degree',)

admin.site.register(Athlete, AthleteAdmin)
admin.site.register(Nutritionist, NutritionistAdmin)
