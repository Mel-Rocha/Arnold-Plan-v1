# apps/core/permissions.py

from rest_framework.permissions import BasePermission

class IsNutritionistUser(BasePermission):
    """
        Permite acesso aos utilizadores Nutricionistas
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_nutritionist

class IsAthleteUser(BasePermission):
    """
        Permite acesso aos utilizadores Atletas
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_athlete