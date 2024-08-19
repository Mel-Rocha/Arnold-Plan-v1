from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.macros_sheet.views import MacrosSheetViewSet

router = DefaultRouter()
router.register(r'', MacrosSheetViewSet, basename='macros_sheet')

urlpatterns = [
    path('', include(router.urls)),
]
