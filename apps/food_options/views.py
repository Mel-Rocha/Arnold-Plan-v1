from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS

from apps.food_options.models import FoodOptions
from apps.food_options.serializers import FoodOptionsSerializer
from apps.core.permissions import IsAthleteUser, IsNutritionistUser


class FoodOptionsViewSet(viewsets.ModelViewSet):
    queryset = FoodOptions.objects.all()
    serializer_class = FoodOptionsSerializer

    def perform_create(self, serializer):
        meal_id = self.kwargs['meal_id']  # Assumindo que o meal_id é passado na URL
        serializer.save(context={'meal_id': meal_id})