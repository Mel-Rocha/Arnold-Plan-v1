from django.contrib import admin
from .models import GeneralInfo

class GeneralInfoAdmin(admin.ModelAdmin):
    list_display = ('goal', 'initial_date', 'final_date', 'weeks')

admin.site.register(GeneralInfo, GeneralInfoAdmin)