from django.urls import path
from app.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home_page'),
    path('users/', UserView.as_view(), name='users')
]