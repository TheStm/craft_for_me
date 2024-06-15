from django.urls import path
from app.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home_page'),
    path('users/', UserView.as_view(), name='users'),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('protected/', ProtectedView.as_view(), name='protected_view')
]