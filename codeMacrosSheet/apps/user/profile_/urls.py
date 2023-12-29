from django.urls import path
from . import views
from .views import CustomLoginView

app_name = 'profile_'

urlpatterns = [
    path('accounts/login/', CustomLoginView.as_view(), name='account_login'),
    path('profile/create/', views.profile_create, name='profile_create'),
    path('profile/<int:pk>/update/', views.profile_update, name='profile_update'),
    path('profile/<int:pk>/delete/', views.profile_delete, name='profile_delete'),
    path('profile/<int:pk>/details/', views.profile_details, name='profile_details'),
]

