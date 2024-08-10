from django.contrib import admin

from apps.user.profile_.models import Profile
from apps.macros.macros_planner.models import MacrosPlanner


class MacrosPlannerInline(admin.TabularInline):
    model = MacrosPlanner


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date', 'weight', 'height', 'gender', 'user')
    inlines = [MacrosPlannerInline]


admin.site.register(Profile, ProfileAdmin)
