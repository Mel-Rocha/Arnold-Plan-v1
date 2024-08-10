from django.urls import path

from .views import statistics_view, statistics_list

app_name = 'statistics_'

urlpatterns = [
    path('statistics_/<int:pk>/', statistics_view, name='statistics_view'),
    path('statistics_list/', statistics_list, name='statistics_list'),
]
