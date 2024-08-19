from rest_framework import serializers

from apps.food_options.models import FoodOptions


class FoodOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodOptions
        fields = '__all__'
