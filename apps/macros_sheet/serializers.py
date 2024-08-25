from rest_framework import serializers

from apps.macros_planner.models import MacrosPlanner
from apps.macros_sheet.models import MacrosSheet


class MacrosSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MacrosSheet
        fields = '__all__'
        extra_kwargs = {
            'macros_planner': {'read_only': True}  # MacrosPlanner é read-only e será definido automaticamente
        }

    def create(self, validated_data):
        macros_planner_id = self.context.get('macros_planner_id')
        macros_planner = MacrosPlanner.objects.get(id=macros_planner_id)

        # Remover 'macros_planner' de validated_data se ele existir
        validated_data.pop('macros_planner', None)

        return MacrosSheet.objects.create(macros_planner=macros_planner, **validated_data)
