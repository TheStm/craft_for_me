from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from . models import *
from . serializer import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from rest_framework import status
from . serializer import MyTokenObtainPairSerializer


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


class HomeView(generics.GenericAPIView):
    def get(self, request):
        return Response({'message': 'Hello, Welcome to home page'})

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "This is a protected view"})
    
    from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = MyTokenObtainPairSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)