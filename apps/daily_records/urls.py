from django.urls import path

from . import views

app_name = 'daily_records'
urlpatterns = [
    path('daily_records/create/', views.create_daily_records, name='create_daily_records'),
    path('daily_records/list/', views.daily_records_list, name='daily_records_list'),
]
