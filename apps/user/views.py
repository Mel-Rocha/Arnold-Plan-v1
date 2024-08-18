from rest_framework import status
from django.db import IntegrityError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

from apps.core import gateway
from apps.user.models import User
from apps.core.gateway import response_log_user
from apps.user.serializers import MyTokenObtainPairSerializer, UpdatePasswordSerializer, \
    UserSerializerCreateOrUpdate, NutritionistSerializerCreateOrUpdate, AthleteSerializerCreateOrUpdate


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class UpdatePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request, *args, **kwargs):
        serializer = UpdatePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({"detail": "Password updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserCreateView(gateway.Create):
    permission_classes = []
    serializer_class = UserSerializerCreateOrUpdate

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            user_data = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'is_staff': user.is_staff,
                'is_superuser': user.is_superuser,
                'is_active': user.is_active,
                'is_nutritionist': user.is_nutritionist,
                'is_athlete': user.is_athlete,
            }
            return response_log_user(request, user_data, 201)
        except IntegrityError:
            return response_log_user(request, "Integrity error.", 409)
        except Exception as e:
            return response_log_user(request, str(e), 400)


# Athlete
class AthleteProfileCreateView(gateway.Create):
    permission_classes = []
    queryset = User.objects.filter(is_active=True)
    serializer_class = AthleteSerializerCreateOrUpdate


class AthleteProfileRetrieveView(gateway.Retrieve):
    permission_classes = []
    queryset = User.objects.filter(is_active=True)
    serializer_class = AthleteSerializerCreateOrUpdate


class AthleteProfileUpdateView(gateway.Update):
    permission_classes = []
    queryset = User.objects.filter(is_active=True)
    serializer_class = AthleteSerializerCreateOrUpdate


class AthleteProfileDestroyView(gateway.Destroy):
    permission_classes = []
    queryset = User.objects.filter(is_active=True)
    serializer_class = AthleteSerializerCreateOrUpdate


class AthleteProfileListView(gateway.List):
    permission_classes = []
    queryset = User.objects.filter(is_active=True)
    serializer_class = AthleteSerializerCreateOrUpdate


# Nutritionist
class NutritionistProfileCreateView(gateway.Create):
    permission_classes = []
    queryset = User.objects.filter(is_active=True)
    serializer_class = NutritionistSerializerCreateOrUpdate


class NutritionistProfileRetrieveView(gateway.Retrieve):
    permission_classes = []
    queryset = User.objects.filter(is_active=True)
    serializer_class = NutritionistSerializerCreateOrUpdate


class NutritionistProfileUpdateView(gateway.Update):
    permission_classes = []
    queryset = User.objects.filter(is_active=True)
    serializer_class = NutritionistSerializerCreateOrUpdate


class NutritionistProfileDestroyView(gateway.Destroy):
    permission_classes = []
    queryset = User.objects.filter(is_active=True)
    serializer_class = NutritionistSerializerCreateOrUpdate


class NutritionistProfileListView(gateway.List):
    permission_classes = []
    queryset = User.objects.filter(is_active=True)
    serializer_class = NutritionistSerializerCreateOrUpdate
