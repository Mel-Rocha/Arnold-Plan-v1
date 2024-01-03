from django.urls import path
from .views import google_fit_auth

urlpatterns = [
    path('google-fit-auth/', google_fit_auth, name='google_fit_auth'),
    path('test_api_request/', test_api_request, name='test_api_request'),
    path('oauth2callback/', oauth2callback, name='oauth2callback'),
]