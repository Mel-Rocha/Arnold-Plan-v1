from rest_framework.permissions import BasePermission

class IsNutritionistUser(BasePermission):
    """
    Allows access to Nutritionist users
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_nutritionist

class IsAthleteUser(BasePermission):
    """
    Allows access to Athlete users
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_athlete