from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, LoginSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate # since we are using in built User model
from rest_framework import generics
# Create your views here.


class RegisterAPI(generics.CreateAPIView):
    serializer_class = UserSerializer
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username = serializer.data['username'])
            refresh = RefreshToken.for_user(user)
            return Response({
                'status' : 200,
                'body' : serializer.data,
                'refresh' : str(refresh),
                'access' : str(refresh.access_token),
                'message' : 'Registration Successfull'
            })
        return Response({
                'status' : 400,
                'message' : 'Something Went Wrong! Data not Valid',
                'data' : serializer.errors
            })

class LoginAPI(generics.CreateAPIView):
    serializer_class = LoginSerializer
    def post(self, request):
        serializer = LoginSerializer(data = request.data)
        if serializer.is_valid(raise_exception = True):
            username = serializer.data['username']
            password = serializer.data['password']
            print(username, password)
            user = authenticate(username=username, password=password)
            
            if user is None:
                return Response({
                    'status' : 400,
                    'message' : 'Invalid Credentials!'
                })
            refresh = RefreshToken.for_user(user)
            return Response({
                'status' : 200,
                'refresh' : str(refresh),
                'access' : str(refresh.access_token),
                'message' : 'Login Successfull'
            })
        return Response({
            'status' : 400,
            'message' : 'Invalid Credentials!',
            'data' : serializer.errors
        })



class UserOPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        user_id = request.user.id
        user = User.objects.get(id = user_id)
        user.delete()
        return Response({
            'status' : 201,
            'message' : 'User Removed',
        })

    # def put(self, request):
    #     serializer = LoginSerializer(data = request.data)
    #     if serializer.is_valid():
    #         username = serializer.data['username']
    #         password = serializer.data['password']
        
    #         user = authenticate(username=username, password=password)
            
    #         if user is None:
    #             return Response({
    #                 'status' : 400,
    #                 'message' : 'Invalid Credentials!'
    #             })
    #         refresh = RefreshToken.for_user(user)
    #         return Response({
    #             'status' : 200,
    #             'refresh' : str(refresh),
    #             'access' : str(refresh.access_token),
    #             'message' : 'Login Successfull'
    #         })
    #     return Response({
    #         'status' : 400,
    #         'message' : 'Invalid Credentials!',
    #         'data' : serializer.errors
    #     })