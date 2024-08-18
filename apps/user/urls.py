from django.urls import path

from apps.user.views import (MyTokenObtainPairView, UpdatePasswordView, AthleteProfileUpdateView,
                             NutritionistProfileUpdateView,
                             UserCreateView, AthleteProfileCreateView, NutritionistProfileCreateView,
                             AthleteProfileRetrieveView, AthleteProfileDestroyView, AthleteProfileListView,
                             NutritionistProfileRetrieveView, NutritionistProfileListView,
                             NutritionistProfileDestroyView)

token_and_passwords = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('password/update/', UpdatePasswordView.as_view(), name='password_update'),
]

user_crud = [
    path('user/create/', UserCreateView.as_view({'post': 'create'}), name='user-create'),
]

atlhlete_crud = [
    path('athlete/create/', AthleteProfileCreateView.as_view({'post': 'create'}), name='athlete-profile-create'),
    path('athlete/retrieve/', AthleteProfileRetrieveView.as_view({'get': 'retrieve'}), name='athlete-retrieve'),
    path('athlete/update/', AthleteProfileUpdateView.as_view({'post': 'update'}), name='athlete-update'),
    path('athlete/destroy/', AthleteProfileDestroyView.as_view({'delete': 'destroy'}), name='athlete-destroy'),
    path('athlete/list/', AthleteProfileListView.as_view({'get': 'list'}), name='athlete-list'),
]

nutritionist_crud = [
    path('nutritionist/create/', NutritionistProfileCreateView.as_view({'post': 'create'}), name='nutritionist-profile-create'),
    path('nutritionist/retrieve/', NutritionistProfileRetrieveView.as_view({'get': 'retrieve'}), name='nutritionist-retrieve'),
    path('nutritionist/update/', NutritionistProfileUpdateView.as_view({'post': 'update'}), name='nutritionist-update'),
    path('nutritionist/destroy/', NutritionistProfileDestroyView.as_view({'delete': 'destroy'}), name='nutritionist-destroy'),
    path('nutritionist/list/', NutritionistProfileListView.as_view({'get': 'list'}), name='nutritionist-list'),
]


urlpatterns = token_and_passwords + user_crud + atlhlete_crud + nutritionist_crud
