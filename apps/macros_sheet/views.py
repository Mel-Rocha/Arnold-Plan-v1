from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS

from apps.macros_sheet.models import MacrosSheet
from apps.macros_sheet.serializers import MacrosSheetSerializer
from apps.core.permissions import IsAthleteUser, IsNutritionistUser


class MacrosSheetViewSet(viewsets.ModelViewSet):
    queryset = MacrosSheet.objects.all()
    serializer_class = MacrosSheetSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [IsAuthenticated(), IsAthleteUser()]
        return [IsAuthenticated(), IsNutritionistUser()]
