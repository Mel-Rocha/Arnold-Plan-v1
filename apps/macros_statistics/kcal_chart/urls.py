from django.urls import path

from .views import kcal_chart_view

app_name = 'kcal_chart'

urlpatterns = [
    path('kcal_chart/<int:pk>/', kcal_chart_view, name='kcal_chart'),
]
