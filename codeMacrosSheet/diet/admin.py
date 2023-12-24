from django.contrib import admin
from .models import Diet
from diet_general_info.models import DietGeneralInfo

class DietGeneralInfoInline(admin.TabularInline):
    model = DietGeneralInfo

class DietAdmin(admin.ModelAdmin):
    list_display = ['id', 'profile']
    inlines = [DietGeneralInfoInline]

admin.site.register(Diet, DietAdmin)