from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.daily_records.views import DailyRecordsViewSet

router = DefaultRouter()
router.register(r'', DailyRecordsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
