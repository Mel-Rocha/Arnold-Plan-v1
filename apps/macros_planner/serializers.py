from rest_framework import serializers

from apps.diet.models import Diet
from apps.diet.serializers import DietSerializer
from apps.macros_planner.models import MacrosPlanner


class MacrosPlannerSerializer(serializers.ModelSerializer):
    diets = DietSerializer(many=True, required=False)

    class Meta:
        model = MacrosPlanner
        fields = '__all__'

    def create(self, validated_data):
        diets_data = validated_data.pop('diets', [])
        macros_planner = MacrosPlanner.objects.create(**validated_data)
        for diet_data in diets_data:
            Diet.objects.create(macros_planner=macros_planner, **diet_data)
        return macros_planner

    def update(self, instance, validated_data):
        diets_data = validated_data.pop('diets', [])
        instance = super().update(instance, validated_data)

        for diet_data in diets_data:

            diet_id = diet_data.get('id')
            if diet_id:
                diet = Diet.objects.get(id=diet_id, macros_planner=instance)
                diet.name = diet_data.get('name', diet.name)
                diet.calories = diet_data.get('calories', diet.calories)

                diet.save()
            else:
                Diet.objects.create(macros_planner=instance, **diet_data)

        return instance
