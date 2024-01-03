from django.contrib import admin
from .models import UserCredentials

class UserCredentialsAdmin(admin.ModelAdmin):
    list_display = ('user', 'credentials_json')#Define os campos visiveis ao adm

admin.site.register(UserCredentials, UserCredentialsAdmin)