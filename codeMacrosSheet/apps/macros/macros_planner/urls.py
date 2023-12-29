from django.urls import path
from . import views

app_name = 'macros_planner'

urlpatterns = [
    path('macros_planner/list/', views.macros_planner_list, name='macros_planner_list'),
    path('macros_planner/create/', views.macros_planner_create, name='macros_planner_create'),
    path('macros_planner/<int:pk>/update/', views.macros_planner_update, name='macros_planner_update'),
    path('macros_planner/<int:pk>/delete/', views.macros_planner_delete, name='macros_planner_delete'),
    path('macros_planner/<int:pk>/details/', views.macros_planner_details, name='macros_planner_details'),
]
