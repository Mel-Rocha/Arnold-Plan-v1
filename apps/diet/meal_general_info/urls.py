from django.urls import path

from . import views

app_name = 'meal_general_info'

urlpatterns = [
    path('meal_general_info/create/', views.meal_general_info_create, name='meal_general_info_create'),
    path('meal_general_info/<int:pk>/update/', views.meal_general_info_update, name='meal_general_info_update'),
    path('meal_general_info/<int:pk>/delete/', views.meal_general_info_delete, name='meal_general_info_delete'),
    path('meal_general_info/<int:pk>/details/', views.meal_general_info_details, name='meal_general_info_details'),
]
