from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date', 'weight', 'height', 'gender', 'user' )

admin.site.register(Profile, ProfileAdmin)
