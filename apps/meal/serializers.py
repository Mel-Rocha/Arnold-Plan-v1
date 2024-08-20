from rest_framework import serializers

from apps.diet.models import Diet
from apps.meal.models import Meal


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'
        extra_kwargs = {
            'diet': {'read_only': True}
        }

    def create(self, validated_data):
        diet_id = self.context['diet_id']
        diet = Diet.objects.get(id=diet_id)
        return Meal.objects.create(diet=diet, **validated_data)
