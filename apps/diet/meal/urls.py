from django.urls import path

from . import views

app_name = 'meal'

urlpatterns = [
    path('meal/list', views.meal_list, name='meal_list'),
    path('meal/create/<int:diet_id>/', views.meal_create, name='meal_create'),
    path('meal/<int:pk>/update/', views.meal_update, name='meal_update'),
    path('meal/<int:pk>/delete/', views.meal_delete, name='meal_delete'),
    path('meal/<int:pk>/details/', views.meal_details, name='meal_details'),

]
