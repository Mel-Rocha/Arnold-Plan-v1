from django.urls import path
from . import views

app_name = 'macros_sheet'

urlpatterns = [
    path('macros_sheet/list/', views.macros_sheet_list, name='macros_sheet_list'),
    path('macros_sheet/<int:pk>/update/', views.macros_sheet_update, name='macros_sheet_update'),
    path('macros_sheet/<int:pk>/details/', views.macros_sheet_details, name='macros_sheet_details'),
]
