from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.food_options.views import FoodOptionsViewSet

router = DefaultRouter()
router.register(r'macros-planner/(?P<macros_planner_id>\d+)/diets/(?P<diet_id>\d+)/meals/(?P<meal_id>\d+)/'
                r'food-options', FoodOptionsViewSet, basename='food-options')

urlpatterns = [
    path('', include(router.urls)),
]
