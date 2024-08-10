from django.urls import path
from . import views

app_name = 'diet_general_info'

urlpatterns = [
    path('diet_general_info/create/', views.diet_general_info_create, name='diet_general_info_create'),
    path('diet_general_info/<int:pk>/update/', views.diet_general_info_update, name='diet_general_info_update'),
    path('diet_general_info/<int:pk>/delete/', views.diet_general_info_delete, name='diet_general_info_delete'),
    path('diet_general_info/<int:pk>/details/', views.diet_general_info_details, name='diet_general_info_details'),
]
