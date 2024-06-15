from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from . models import *
from . serializer import *
from rest_framework.response import Response

class UserView(generics.ListCreateAPIView):
    # def get(self, request):
    #     output = [{'username': user.username, 'email': user.email} for user in User.objects.all()]
    #     return Response(output)

    # def post(self, request):
    #     user = request.data
    #     serializer = UserSerializer(data=user)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data)
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Create your views here.
