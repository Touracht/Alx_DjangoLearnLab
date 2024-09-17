from rest_framework import serializers
from .models import CustomUser

class CustomRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    model = CustomUser
    fields = ['username', 'password', 'password2', 'bio', 'profile_picture', 'followers']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password': 'Passwords must match'})
        
    def create(self, validated_data):
        validated_data.pop('password2')
        user = CustomUser(username = validated_data['username'])
