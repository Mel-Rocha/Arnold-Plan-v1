from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS

from apps.diet.models import Diet
from apps.diet.serializers import DietSerializer
from apps.core.permissions import IsAthleteUser, IsNutritionistUser

class DietViewSet(viewsets.ModelViewSet):
    queryset = Diet.objects.all()
    serializer_class = DietSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [IsAuthenticated(), IsAthleteUser()]
        return [IsAuthenticated(), IsNutritionistUser()]
