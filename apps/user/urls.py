from django.urls import path

from apps.user.views import MyTokenObtainPairView, UpdatePasswordView, AthleteCreateView, NutritionistCreateView, UserCreateView

token_and_passwords = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('password/update/', UpdatePasswordView.as_view(), name='password_update'),
]

create_users = [
    path('user/create/', UserCreateView.as_view(), name='user_create'),
    path('athlete/create/', AthleteCreateView.as_view(), name='athlete_create'),
    path('nutritionist/create/', NutritionistCreateView.as_view(), name='nutritionist_create'),
]

urlpatterns = token_and_passwords + create_users
