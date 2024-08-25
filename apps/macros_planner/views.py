from rest_framework import viewsets, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS

from apps.macros_planner.models import MacrosPlanner
from apps.core.permissions import IsNutritionistUser
from apps.macros_planner.serializers import MacrosPlannerSerializer
from apps.user.models import Nutritionist


class MacrosPlannerViewSet(viewsets.ModelViewSet):
    serializer_class = MacrosPlannerSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [IsAuthenticated()]
        return [IsAuthenticated(), IsNutritionistUser()]

    def get_queryset(self):
        """
        Filtra a queryset para garantir que o usuário autenticado
        só veja os MacrosPlanner aos quais ele está relacionado.
        """
        user = self.request.user

        if user.is_nutritionist:
            # Nutricionista vê apenas os MacrosPlanner dos seus atletas
            return MacrosPlanner.objects.filter(nutritionist__user=user)
        elif user.is_athlete:
            # Atleta vê apenas o seu próprio MacrosPlanner
            return MacrosPlanner.objects.filter(athlete__user=user)
        else:
            return MacrosPlanner.objects.none()

    def retrieve(self, request, *args, **kwargs):
        """
        Sobrescreve o método retrieve para garantir que o usuário só consiga
        acessar MacrosPlanners aos quais ele está relacionado.
        """
        instance = self.get_object()
        user = self.request.user

        if user.is_nutritionist:
            # Nutricionista pode acessar apenas MacrosPlanners dos atletas que ele gerencia
            if instance.nutritionist.user != user:
                raise PermissionDenied("Você não tem permissão para acessar este MacrosPlanner.")
        elif user.is_athlete:
            # Atleta pode acessar apenas seu próprio MacrosPlanner
            if instance.athlete.user != user:
                raise PermissionDenied("Você não tem permissão para acessar este MacrosPlanner.")
        else:
            raise PermissionDenied("Você não tem permissão para acessar este MacrosPlanner.")

        serializer = self.get_serializer(instance)
        return Response(serializer.data)


    def create(self, request, *args, **kwargs):
        """
        Sobrescreve o método create para garantir que apenas nutricionistas
        possam criar MacrosPlanners e apenas para seus próprios atletas.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user

        if user.is_nutritionist:
            athlete_id = serializer.validated_data['athlete'].id
            # Garantir que o nutricionista está criando um MacrosPlanner para um atleta que ele gerencia
            if not Nutritionist.objects.filter(user=user, athletes__id=athlete_id).exists():
                raise PermissionDenied("Você não tem permissão para criar um MacrosPlanner para este atleta.")
        elif user.is_athlete:
            raise PermissionDenied("Você não tem permissão para criar um MacrosPlanner.")

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        """
        Sobrescreve o método update para garantir que apenas nutricionistas
        possam atualizar MacrosPlanners e apenas para seus próprios atletas.
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        user = request.user

        if user.is_nutritionist:
            # Garantir que o nutricionista está atualizando um MacrosPlanner para um atleta que ele gerencia
            if instance.nutritionist.user != user:
                raise PermissionDenied("Você não tem permissão para atualizar este MacrosPlanner.")
        elif user.is_athlete:
            raise PermissionDenied("Você não tem permissão para atualizar um MacrosPlanner.")

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """
        Sobrescreve o método destroy para garantir que apenas nutricionistas
        possam excluir MacrosPlanners e apenas para seus próprios atletas.
        """
        instance = self.get_object()
        user = request.user

        if user.is_nutritionist:
            # Garantir que o nutricionista está excluindo um MacrosPlanner para um atleta que ele gerencia
            if instance.nutritionist.user != user:
                raise PermissionDenied("Você não tem permissão para excluir este MacrosPlanner.")
        elif user.is_athlete:
            raise PermissionDenied("Você não tem permissão para excluir um MacrosPlanner.")

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)