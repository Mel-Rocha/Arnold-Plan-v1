from django.contrib import admin
from .models import MacrosPlanner
from macros_sheet.models import MacrosSheet

class MacrosSheetInline(admin.TabularInline):
    model = MacrosSheet

class MacrosPlannerAdmin(admin.ModelAdmin):
    list_display = ['profile']
    inlines = [MacrosSheetInline]

admin.site.register(MacrosPlanner, MacrosPlannerAdmin)
