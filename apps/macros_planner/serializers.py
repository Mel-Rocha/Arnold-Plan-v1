from rest_framework import serializers

from apps.diet.serializers import DietSerializer
from apps.macros_planner.models import MacrosPlanner
from apps.user.models import Nutritionist


class MacrosPlannerSerializer(serializers.ModelSerializer):
    diets = DietSerializer(many=True, required=False)

    class Meta:
        model = MacrosPlanner
        fields = '__all__'
        extra_kwargs = {
            'nutritionist': {'read_only': True},
        }

    def create(self, validated_data):
        diets_data = validated_data.pop('diets', [])

        # Obtenha o user logado
        user = self.context['request'].user

        # Encontre o Nutritionist associado ao user logado
        try:
            nutritionist = Nutritionist.objects.get(user=user)
        except Nutritionist.DoesNotExist:
            raise serializers.ValidationError({'nutritionist': 'Nutritionist with the current user does not exist.'})

        # Crie o MacrosPlanner e associe o Nutritionist encontrado
        macros_planner = MacrosPlanner.objects.create(nutritionist=nutritionist, **validated_data)

        # Atualize o contexto com o novo ID do MacrosPlanner
        context = self.context
        context['macros_planner_id'] = macros_planner.id

        # Crie as dietas associadas
        for diet_data in diets_data:
            # Adicione o ID do MacrosPlanner ao contexto da dieta
            diet_data['macros_planner'] = macros_planner.id

            # Crie uma instância do DietSerializer com o contexto correto
            diet_serializer = DietSerializer(data=diet_data, context=context)
            if diet_serializer.is_valid():
                diet_serializer.save()  # Salve a dieta, que também criará meals
            else:
                raise serializers.ValidationError(diet_serializer.errors)

        return macros_planner