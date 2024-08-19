from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.diet.views import DietViewSet

router = DefaultRouter()
router.register(r'diets', DietViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
