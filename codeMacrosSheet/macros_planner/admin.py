from django.contrib import admin
from .models import MacrosPlanner

class MacrosPlannerAdmin(admin.ModelAdmin):
    list_display = []

admin.site.register(MacrosPlanner, MacrosPlannerAdmin)
