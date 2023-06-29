from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include ('all_auth.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    
]