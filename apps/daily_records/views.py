from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS

from apps.daily_records.models import DailyRecords
from apps.daily_records.serializers import DailyRecordsSerializer
from apps.core.permissions import IsAthleteUser, IsNutritionistUser


class DailyRecordsViewSet(viewsets.ModelViewSet):
    queryset = DailyRecords.objects.all()
    serializer_class = DailyRecordsSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [IsAuthenticated(), IsNutritionistUser()]
        return [IsAuthenticated(), IsAthleteUser()]
