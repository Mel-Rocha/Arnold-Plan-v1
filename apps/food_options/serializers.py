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
        meal_id = validated_data.pop('meal_id', None)  # Recuperando meal_id diretamente dos dados validados
        if not meal_id:
            raise serializers.ValidationError("Meal ID is required.")

        # Verifica se a Meal com o ID especificado existe
        try:
            meal = Meal.objects.get(id=meal_id)
        except Meal.DoesNotExist:
            raise serializers.ValidationError(f"Meal with id {meal_id} does not exist.")

        # Criação do objeto FoodOptions com a refeição associada
        return FoodOptions.objects.create(meal=meal, **validated_data)

    def update(self, instance, validated_data):
        validated_data.pop('meal', None)  # Certifica que 'meal' não será atualizado
        return super().update(instance, validated_data)