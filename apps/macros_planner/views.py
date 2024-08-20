from rest_framework import viewsets, status
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


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
