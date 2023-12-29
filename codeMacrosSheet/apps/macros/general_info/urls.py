from django.urls import path
from . import views

app_name = 'general_info'

urlpatterns = [
    path('general_info/create/', views.general_info_create, name='general_info_create'),
    path('general_info/<int:pk>/update/', views.general_info_update, name='general_info_update'),
    path('general_info/<int:pk>/delete/', views.general_info_delete, name='general_info_delete'),
    path('general_info/<int:pk>/details/', views.general_info_details, name='general_info_details'),
]
