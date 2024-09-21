from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from .models import Post, Comment, Like
from django.db.models import Q
from .pagination import CustomPostPagination, CustomCommentPagination
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = [CustomPostPagination]

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [permissions.AllowAny]

        else:
            permission_classes = [permissions.IsAuthenticated]

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
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = [CustomCommentPagination]
        
class FeedView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user

        following_users = user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class LikeView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LikeSerializer

    def post(self, request, pk):
        post_to_like = generics.get_object_or_404(Post, pk=pk)
       
        like_instance, created = Like.objects.get_or_create(user = request.user, post = post_to_like)

        if created:
            return Response({'detail': 'You have successfully liked this post'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'detail': 'You have already liked this post'}, status=status.HTTP_400_BAD_REQUEST)
        
class UnlikeView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
    
        like_instance, created = Like.objects.get_or_create(user=request.user, post=post)

        if created:
            return Response({"detail": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        else:
            like_instance.delete()
            return Response({"detail": "Post unliked successfully."}, status=status.HTTP_200_OK)





