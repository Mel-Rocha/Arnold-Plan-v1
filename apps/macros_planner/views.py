from rest_framework import viewsets, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS

from apps.macros_planner.models import MacrosPlanner
from apps.core.permissions import IsNutritionistUser
from apps.macros_planner.serializers import MacrosPlannerSerializer


class MacrosPlannerViewSet(viewsets.ModelViewSet):
    queryset = MacrosPlanner.objects.all()
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
        acessar MacrosPlanner aos quais ele está relacionado.
        """
        instance = self.get_object()
        user = self.request.user

        if user.is_nutritionist and instance.nutritionist.user != user:
            raise PermissionDenied("Você não tem permissão para acessar este MacrosPlanner.")
        elif user.is_athlete and instance.athlete.user != user:
            raise PermissionDenied("Você não tem permissão para acessar este MacrosPlanner.")

        serializer = self.get_serializer(instance)
        return Response(serializer.data)


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
