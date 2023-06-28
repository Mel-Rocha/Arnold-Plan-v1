from django.contrib import admin
from .models import MacrosSheet

class MacrosSheetAdmin(admin.ModelAdmin):
    list_display = ('cho', 'ptn', 'fat', 'kcal', 'kcal_level', 'cho_level', 'ptn_level', 'fat_level')

admin.site.register(MacrosSheet, MacrosSheetAdmin)

