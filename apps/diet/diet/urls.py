from django.urls import path
from . import views

app_name = 'diet'

urlpatterns = [
    path('diet/list', views.diet_list, name='diet_list'),
    path('diet/create/', views.diet_create, name='diet_create'),
    path('diet/<int:pk>/update/', views.diet_update, name='diet_update'),
    path('diet/<int:pk>/delete/', views.diet_delete, name='diet_delete'),
    path('diet/<int:pk>/details/', views.diet_details, name='diet_details'),
]
