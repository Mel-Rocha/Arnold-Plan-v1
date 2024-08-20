from rest_framework import viewsets

from apps.meal.models import Meal
from apps.meal.serializers import MealSerializer


class MealViewSet(viewsets.ModelViewSet):
    serializer_class = MealSerializer

    def get_queryset(self):
        return Meal.objects.filter(diet=self.kwargs['diet_id'])

    def perform_create(self, serializer):
        serializer.context['diet_id'] = self.kwargs['diet_id']
        serializer.save()
