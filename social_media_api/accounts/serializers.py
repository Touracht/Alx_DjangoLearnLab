from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

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
        user = CustomUser.objects.create_user(username = validated_data['username'],
                          bio = validated_data.get('bio', ''),
                          profile_picture = validated_data.get('profile_picture', None))
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):

        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError('Invalid username or password')
        
        data['user'] = user
        return data
    
    def create(self, validated_data):
        user = validated_data['user']

        Token.objects.create(user=user)

        token, created = Token.objects.get_or_create(user=user)
        return {'token': token.key}
    

        
