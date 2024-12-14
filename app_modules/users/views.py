from django.shortcuts import render
from app_modules.users import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate,login
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

class UserRegisterView(APIView):

    serializer_class = serializers.UserRegistrationsSerailizer

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "message":"User Registered Successfully..."
            },
            status=status.HTTP_201_CREATED
        )

class UserLoginView(APIView):

    serializer_class = serializers.UserLoginSerializer


    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            email  = serializer.validated_data["email"],
            password  = serializer.validated_data["password"],
        )
        if user:
            login(request,user)
            refresh = RefreshToken.for_user(user)

            return Response(
                {
                    "message":"Login Successfull...",
                    "refresh" : str(refresh),
                    "access" : str(refresh.access_token),
                },
                status=status.HTTP_200_OK
            )
        
        return Response(
        {
            "message":"User Not Found...",
        },
        status=status.HTTP_204_NO_CONTENT
        )
        