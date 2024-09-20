from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CustomRegisterSerializer, LoginSerializer, ProfileSerializer
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
def register_user(request):
    serializer = CustomRegisterSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()

        return Response({'message': 'User has been created successfully', 'id': user.id}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def login_user(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProfileView(generics.RetrieveUpdateAPIView):

    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user





