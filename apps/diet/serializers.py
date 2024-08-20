from rest_framework import serializers

from apps.diet.models import Diet
from apps.macros_planner.models import MacrosPlanner
from apps.meal.models import Meal
from apps.meal.serializers import MealSerializer


class DietSerializer(serializers.ModelSerializer):
    meals = MealSerializer(many=True, required=False)  # Campo relacionado

    class Meta:
        model = Diet
        fields = '__all__'
        extra_kwargs = {
            'macros_planner': {'read_only': True}
        }

    def create(self, validated_data):
        # Remove `meals` dos dados validados antes de criar o `Diet`
        meals_data = validated_data.pop('meals', [])

        # Obtenha o `macros_planner` usando o contexto
        macros_planner_id = self.context['macros_planner_id']
        macros_planner = MacrosPlanner.objects.get(id=macros_planner_id)

        # Crie o objeto `Diet` sem passar `meals`
        diet = Diet.objects.create(macros_planner=macros_planner, **validated_data)

        # Crie os objetos `Meal` associados ao `Diet`
        for meal_data in meals_data:
            Meal.objects.create(diet=diet, **meal_data)

        return diet

    def update(self, instance, validated_data):
        # Remove `meals` dos dados validados antes de atualizar o `Diet`
        meals_data = validated_data.pop('meals', [])

        # Atualiza o objeto `Diet`
        instance = super().update(instance, validated_data)

        # Atualize ou crie os objetos `Meal` associados ao `Diet`
        for meal_data in meals_data:
            meal_id = meal_data.get('id')
            if meal_id:
                # Se o `meal` já existe, atualize-o
                meal = Meal.objects.get(id=meal_id, diet=instance)
                for key, value in meal_data.items():
                    setattr(meal, key, value)
                meal.save()
            else:
                # Se o `meal` não existe, crie um novo
                Meal.objects.create(diet=instance, **meal_data)

        return instance
