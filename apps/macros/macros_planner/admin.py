from django.contrib import admin

from apps.macros.macros_sheet.models import MacrosSheet
from apps.macros.general_info.models import GeneralInfo
from apps.macros.macros_planner.models import MacrosPlanner


class MacrosSheetInline(admin.TabularInline):
    model = MacrosSheet


class GeneralInfoInline(admin.TabularInline):
    model = GeneralInfo


class MacrosPlannerAdmin(admin.ModelAdmin):
    list_display = ['id', 'profile']
    inlines = [MacrosSheetInline, GeneralInfoInline]


admin.site.register(MacrosPlanner, MacrosPlannerAdmin)
