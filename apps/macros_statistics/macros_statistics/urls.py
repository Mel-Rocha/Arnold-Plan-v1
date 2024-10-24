from django.urls import path

from .views import view_macros_tuples

urlpatterns = [
    # Outras URLs do seu aplicativo
    path('macros_planner/<int:pk>/macros_tuples/', view_macros_tuples, name='macros_tuples'),
]
