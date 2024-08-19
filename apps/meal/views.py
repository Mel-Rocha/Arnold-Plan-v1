from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS

from apps.meal.models import Meal
from apps.meal.serializers import MealSerializer
from apps.core.permissions import IsAthleteUser, IsNutritionistUser


class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [IsAuthenticated(), IsAthleteUser()]
        return [IsAuthenticated(), IsNutritionistUser()]
