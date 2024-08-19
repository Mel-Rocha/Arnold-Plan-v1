from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.food_options.views import FoodOptionsViewSet

router = DefaultRouter()
router.register(r'', FoodOptionsViewSet, basename='food_options')

urlpatterns = [
    path('', include(router.urls)),
]
