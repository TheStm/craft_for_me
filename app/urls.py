from django.urls import path
from app.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home_page'),
    # path('user/', UserView.as_view(), name='user'),
    path('protected/', ProtectedView.as_view(), name='protected_view'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),   
]