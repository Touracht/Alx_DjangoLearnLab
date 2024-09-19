from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CustomRegisterSerializer, LoginSerializer
from rest_framework import status

@api_view(['POST'])
def register_user(request):
    serializer = CustomRegisterSerializer
    if serializer.is_valid():
        user = serializer.save()

        return Response({'message': 'User has been created successfully'}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def login_user(request):
    serializer = LoginSerializer
    if serializer.is_valid():
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



