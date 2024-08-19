from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS

from apps.macros_planner.models import MacrosPlanner
from apps.macros_planner.serializers import MacrosPlannerSerializer
from apps.core.permissions import IsAthleteUser, IsNutritionistUser


class MacrosPlannerViewSet(viewsets.ModelViewSet):
    queryset = MacrosPlanner.objects.all()
    serializer_class = MacrosPlannerSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [IsAuthenticated(), IsAthleteUser()]
        return [IsAuthenticated(), IsNutritionistUser()]
