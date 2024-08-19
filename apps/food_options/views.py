from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS

from apps.food_options.models import FoodOptions
from apps.food_options.serializers import FoodOptionsSerializer
from apps.core.permissions import IsAthleteUser, IsNutritionistUser


class FoodOptionsViewSet(viewsets.ModelViewSet):
    queryset = FoodOptions.objects.all()
    serializer_class = FoodOptionsSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [IsAuthenticated(), IsNutritionistUser()]
        return [IsAuthenticated(), IsAthleteUser()]
