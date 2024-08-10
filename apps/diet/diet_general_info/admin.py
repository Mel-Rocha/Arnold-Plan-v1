from django.contrib import admin

from apps.diet.diet_general_info.models import DietGeneralInfo


class DietGeneralInfoAdmin(admin.ModelAdmin):
    list_display = ('goal', 'observations', 'initial_date', 'final_date', 'weeks', 'type_of_diet')


admin.site.register(DietGeneralInfo, DietGeneralInfoAdmin)
