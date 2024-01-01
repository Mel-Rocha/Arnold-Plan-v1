from django.contrib import admin
from .models import Profile
from macros_planner.models import MacrosPlanner

class MacrosPlannerInline(admin.TabularInline):
    model = MacrosPlanner

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date', 'weight', 'height', 'gender', 'user' )
    inlines = [MacrosPlannerInline]

admin.site.register(Profile, ProfileAdmin)
