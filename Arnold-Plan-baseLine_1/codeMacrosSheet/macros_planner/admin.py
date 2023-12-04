from django.contrib import admin
from .models import MacrosPlanner
from macros_sheet.models import MacrosSheet
from general_info.models import GeneralInfo

class MacrosSheetInline(admin.TabularInline):
    model = MacrosSheet

class GeneralInfoInline(admin.TabularInline):
    model = GeneralInfo

class MacrosPlannerAdmin(admin.ModelAdmin):
    list_display = ['id', 'profile']
    inlines = [MacrosSheetInline, GeneralInfoInline]

admin.site.register(MacrosPlanner, MacrosPlannerAdmin)
