from django.urls import path
from . import views

app_name = 'food_options'

urlpatterns = [
    path('meal/<int:meal_id>/food_options/create/', views.food_options_create, name='food_options_create'),
    path('food_options_list/<int:pk>/', views.food_options_list, name='food_options_list'),
    path('food_options/<int:pk>/update/', views.food_options_update, name='food_options_update'),
    path('food_options/<int:pk>/details/', views.food_options_details, name='food_options_details'),
    path('food_options/<int:pk>/delete/', views.food_options_delete, name='food_options_delete'),
]
