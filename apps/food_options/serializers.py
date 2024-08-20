from rest_framework import serializers

from apps.food_options.models import FoodOptions
from apps.meal.models import Meal


class FoodOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodOptions
        fields = '__all__'
        extra_kwargs = {
            'meal': {'read_only': True}  # Meal is read-only and will be set automatically
        }

    def create(self, validated_data):
        meal_id = self.context['meal_id']  # Assumes meal_id is passed in context
        meal = Meal.objects.get(id=meal_id)

        return FoodOptions.objects.create(meal=meal, **validated_data)

    def update(self, instance, validated_data):
        validated_data.pop('meal', None)  # Ensure 'meal' is not updated
        return super().update(instance, validated_data)