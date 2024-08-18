from django.urls import path

from .views import MyTokenObtainPairView, UpdatePasswordView


urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('password/update/', UpdatePasswordView.as_view(), name='password_update'),
]