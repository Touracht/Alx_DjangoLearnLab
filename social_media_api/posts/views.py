from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment
from django.db.models import Q
from .pagination import CustomPostPagination, CustomCommentPagination
from rest_framework.response import Response
from rest_framework import generics

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = [CustomPostPagination]

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]

        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.query_params.get('search', None)  
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) | Q(content__icontains=search)
            )
        return queryset

    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = [CustomCommentPagination]
        
class FeedView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        followed_users = user.following.all()
        posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')

        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)