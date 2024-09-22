from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CustomRegisterSerializer, LoginSerializer, ProfileSerializer, FollowingSerializer
from rest_framework import status
from rest_framework import generics
from rest_framework import permissions
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType
from .paginations import UsersPagination

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
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
    
from .models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()

class FollowView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, username):
        user_to_follow = get_object_or_404(CustomUser, username=username)
        
        if user_to_follow != request.user:
            request.user.following.add(user_to_follow)  
            
            content_type = ContentType.objects.get_for_model(user_to_follow)
            Notification.objects.create(
                recipient=user_to_follow,  
                actor=request.user,        
                verb='started following you',
                content_type=content_type,
                object_id=user_to_follow.id,
                read=False
            )
            
            serializer = FollowingSerializer(user_to_follow)
            return Response(
                {
                    'detail': f"You are now following {user_to_follow.username}",
                    'user': serializer.data
                }, 
                status=status.HTTP_200_OK
            )
        else:
            return Response({'detail': "You cannot follow yourself"}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        users = CustomUser.objects.all()
        paginator = UsersPagination()
        paginated_users = paginator.paginate_queryset(users, request)

        usernames = [user.username for user in paginated_users]
        return paginator.get_paginated_response(usernames)

class UnfollowView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, username):
        user_to_unfollow = get_object_or_404(User, username=username)
        if user_to_unfollow != request.user:
            request.user.following.remove(user_to_unfollow)

            return Response(
                {
                    'detail': f"You are now unfollowing {user_to_unfollow.username}"
                }, status=status.HTTP_200_OK
        )
        else:
            return Response({'detail': "You cannot unfollow yourself"}, status=status.HTTP_400_BAD_REQUEST)

        






