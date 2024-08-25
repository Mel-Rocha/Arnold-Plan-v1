from rest_framework import serializers

from apps.daily_records.models import DailyRecords
from apps.user.models import Athlete


class DailyRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyRecords
        fields = '__all__'
        extra_kwargs = {
            'athlete': {'read_only': True},
        }

    def create(self, validated_data):
        request = self.context['request']
        # Obtenha o atleta associado ao usuário logado
        athlete = Athlete.objects.get(user=request.user)
        validated_data['athlete'] = athlete
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Não permitimos alterar o atleta durante a atualização
        validated_data.pop('athlete', None)
        return super().update(instance, validated_data)