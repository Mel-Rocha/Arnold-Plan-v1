from rest_framework import viewsets
from rest_framework.exceptions import NotFound

from apps.diet.models import Diet
from apps.macros_planner.models import MacrosPlanner
from apps.meal.models import Meal
from apps.meal.serializers import MealSerializer


class MealViewSet(viewsets.ModelViewSet):
    serializer_class = MealSerializer

    def get_queryset(self):
        macros_planner_id = self.kwargs.get('macros_planner_id')
        diet_id = self.kwargs.get('diet_id')

        # Verificar se o MacrosPlanner existe
        try:
            macros_planner = MacrosPlanner.objects.get(id=macros_planner_id)
        except MacrosPlanner.DoesNotExist:
            raise NotFound(f'MacrosPlanner with id {macros_planner_id} does not exist')

        # Verificar se a Diet existe e pertence ao MacrosPlanner
        try:
            diet = Diet.objects.get(id=diet_id, macros_planner=macros_planner)
        except Diet.DoesNotExist:
            raise NotFound(f'Diet with id {diet_id} does not exist or does not belong to MacrosPlanner with id {macros_planner_id}')

        # Retornar as refeições relacionadas à Dieta
        return Meal.objects.filter(diet=diet)

    def perform_create(self, serializer):
        macros_planner_id = self.kwargs.get('macros_planner_id')
        diet_id = self.kwargs.get('diet_id')

        # Verificar se o MacrosPlanner existe
        try:
            MacrosPlanner.objects.get(id=macros_planner_id)
        except MacrosPlanner.DoesNotExist:
            raise NotFound(f'MacrosPlanner with id {macros_planner_id} does not exist')

        # Verificar se a Diet existe e pertence ao MacrosPlanner
        try:
            diet = Diet.objects.get(id=diet_id, macros_planner__id=macros_planner_id)
        except Diet.DoesNotExist:
            raise NotFound(f'Diet with id {diet_id} does not exist or does not belong to MacrosPlanner with id {macros_planner_id}')

        # Passar diet_id para o contexto do serializer
        serializer.context['diet_id'] = diet_id

        # Salvar a refeição com a dieta associada
        serializer.save(diet=diet)