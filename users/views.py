from django.shortcuts import render
from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework import status
from .serializers import UserSerializer
# Create your views here.
# {
#     "username": admin123,
#     "password": 101010
# }

class LoginView(APIView):
    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)

            return HttpResponse("User's been logged in!", status=status.HTTP_200_OK)
        return HttpResponse("Cannot log in!", status=status.HTTP_403_FORBIDDEN)
    

class RegisterUserView(CreateAPIView):
    model=get_user_model()
    serializer_class=UserSerializer
