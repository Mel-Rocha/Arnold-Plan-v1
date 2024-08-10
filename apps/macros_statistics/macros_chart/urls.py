from django.urls import path

from .views import macros_chart_view, macros_pie_chart_view

app_name = 'macros_chart'

urlpatterns = [
    path('macros_chart/<int:pk>/', macros_chart_view, name='macros_chart'),
    path('macros_pie_chart/<int:sheet_id>/', macros_pie_chart_view, name='macros_pie_chart'),
]
