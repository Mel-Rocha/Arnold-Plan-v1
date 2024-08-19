from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.user.models import Athlete, Nutritionist, User


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        print("Validating with attrs:", attrs)
        data = super().validate(attrs)
        print("Data after validation:", data)
        user = self.user
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
        data.update(user_data)
        return data


class UpdatePasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match")
        return data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'is_active', 'is_nutritionist', 'is_athlete']


class UserSerializerCreateOrUpdate(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        instance.save()
        return instance


class AthleteSerializer(serializers.ModelSerializer):
    user_id = serializers.UUIDField(source='user.id', read_only=True)
    nutritionist_id = serializers.UUIDField(source='nutritionist.id', read_only=True)

    class Meta:
        model = Athlete
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation.pop('user', None)
        representation.pop('nutritionist', None)
        representation.pop('id', None)

        representation['athlete_id'] = instance.id
        representation['user_id'] = instance.user.id
        representation['nutritionist_id'] = instance.nutritionist.id if instance.nutritionist else None

        return representation

    def to_internal_value(self, data):
        internal_data = super().to_internal_value(data)
        user_id = data.get('user_id')
        nutritionist_id = data.get('nutritionist_id')

        if user_id:
            try:
                internal_data['user'] = User.objects.get(id=user_id)
            except User.DoesNotExist:
                raise serializers.ValidationError({'user_id': 'User with this ID does not exist.'})

        if nutritionist_id:
            try:
                internal_data['nutritionist'] = Nutritionist.objects.get(id=nutritionist_id)
            except Nutritionist.DoesNotExist:
                raise serializers.ValidationError({'nutritionist_id': 'Nutritionist with this ID does not exist.'})

        return internal_data


class NutritionistSerializer(serializers.ModelSerializer):
    user_id = serializers.UUIDField(source='user.id', read_only=True)

    class Meta:
        model = Nutritionist
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation.pop('user', None)
        representation.pop('id', None)

        representation['nutritionist_id'] = instance.id
        representation['user_id'] = instance.user.id

        return representation

    def to_internal_value(self, data):
        internal_data = super().to_internal_value(data)
        user_id = data.get('user_id')

        if user_id:
            try:
                internal_data['user'] = User.objects.get(id=user_id)
            except User.DoesNotExist:
                raise serializers.ValidationError({'user_id': 'User with this ID does not exist.'})

        return internal_data
