from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "_all_"
        read_only_fields = ['created_at', 'updated_at']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "_all_"
        read_only_fields = ['created_at', 'updated_at']




