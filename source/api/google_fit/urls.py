from django.urls import path
from .views import google_fit_auth

urlpatterns = [
    path('google-fit-auth/', google_fit_auth, name='google_fit_auth'),
]