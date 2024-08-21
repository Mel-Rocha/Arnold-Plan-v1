from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.meal.views import MealViewSet

router = DefaultRouter()
router.register( r'macros-planners/(?P<macros_planner_id>\d+)/diets/(?P<diet_id>\d+)/meals',
                 MealViewSet, basename='meal')

urlpatterns = [
    path('', include(router.urls)),
]
