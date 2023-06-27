from django.contrib import admin
from .models import MacrosSheet

class MacrosSheetAdmin(admin.ModelAdmin):
    list_display = ('cho', 'ptn', 'fat', 'kcal', 'kcal_level')

admin.site.register(MacrosSheet, MacrosSheetAdmin)

