from rest_framework import serializers

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

        self.context['macros_planner_id'] = macros_planner.id

        for diet_data in diets_data:
            diet_serializer = DietSerializer(data=diet_data, context=self.context)
            if diet_serializer.is_valid():
                diet_serializer.save()
            else:
                raise serializers.ValidationError(diet_serializer.errors)

        return macros_planner
