from django.urls import path
from app.views import *

urlpatterns = [
    path('users/', UserView.as_view(), name='users')
]