from rest_framework import serializers

from apps.macros_planner.models import MacrosPlanner


class MacrosPlannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MacrosPlanner
        fields = '__all__'
