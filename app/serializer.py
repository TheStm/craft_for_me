from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        
        username = attrs.get('username'),
        password = attrs.get('password')
        print(attrs.get('username'))
        print(attrs.get('password'))
        user = authenticate(username=username, password=password)
        print(user)
        if user:
            refresh = self.get_token(user)
            return {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        else:
            raise serializers.ValidationError('Invalid credentials')
