from rest_framework import serializers

from apps.diet.models import Diet
from apps.macros_planner.models import MacrosPlanner


class DietSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diet
        fields = '__all__'
        extra_kwargs = {
            'macros_planner': {'read_only': True}  # Does not allow macros_planner to be passed manually
        }

    def create(self, validated_data):
        # Passing macros_planner automatically
        macros_planner_id = self.context['macros_planner_id']
        macros_planner = MacrosPlanner.objects.get(id=macros_planner_id)
        return Diet.objects.create(macros_planner=macros_planner, **validated_data)


