from rest_framework import serializers

from apps.macros_sheet.models import MacrosSheet


class MacrosSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MacrosSheet
        fields = '__all__'
