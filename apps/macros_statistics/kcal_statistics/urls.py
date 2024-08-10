from django.urls import path

from .views import view_kcal_tuples

urlpatterns = [
    # Outras URLs do seu aplicativo
    path('macros_planner/<int:pk>/kcal_tuples/', view_kcal_tuples, name='macros_planner_kcal_tuples'),
]
