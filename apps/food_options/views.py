from django_rest_passwordreset import serializers
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS

from apps.food_options.models import FoodOptions
from apps.food_options.serializers import FoodOptionsSerializer
from apps.core.permissions import IsAthleteUser, IsNutritionistUser


class FoodOptionsViewSet(viewsets.ModelViewSet):
    queryset = FoodOptions.objects.all()
    serializer_class = FoodOptionsSerializer

    def perform_create(self, serializer):
        meal_id = self.kwargs.get('meal_id')  # Use get para evitar KeyError
        if not meal_id:
            raise serializers.ValidationError("Meal ID is required.")
        print(f"MELA ID: {meal_id}")
        serializer.save(meal_id=meal_id)