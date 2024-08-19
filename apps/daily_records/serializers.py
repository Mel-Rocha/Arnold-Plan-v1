from rest_framework import serializers

from apps.daily_records.models import DailyRecords


class DailyRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyRecords
        fields = '__all__'
