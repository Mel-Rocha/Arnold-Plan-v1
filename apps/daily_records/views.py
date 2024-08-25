from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS

from apps.daily_records.models import DailyRecords
from apps.daily_records.serializers import DailyRecordsSerializer
from apps.core.permissions import IsAthleteUser, IsNutritionistUser
from apps.user.models import Nutritionist


class DailyRecordsViewSet(viewsets.ModelViewSet):
    serializer_class = DailyRecordsSerializer

    def get_queryset(self):
        user = self.request.user

        if user.is_nutritionist:
            try:
                # Obtenha a instância do Nutritionist associado ao usuário
                nutritionist = Nutritionist.objects.get(user=user)
                print(f"Nutritionist instance: {nutritionist}")  # Verificação para debug
                # Filtra os DailyRecords pelos atletas associados ao nutricionista
                return DailyRecords.objects.filter(athlete__nutritionist=nutritionist)
            except Nutritionist.DoesNotExist:
                return DailyRecords.objects.none()  # Retorna vazio se o nutricionista não existir
        elif user.is_athlete:
            # Filtra os DailyRecords apenas para o atleta autenticado
            return DailyRecords.objects.filter(athlete__user=user)
        return DailyRecords.objects.none()

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [IsAuthenticated()]
        return [IsAuthenticated(), IsAthleteUser()]