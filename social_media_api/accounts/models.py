from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The username field must be set')
        user = self.model(username=username, **extra_fields)
        return user
    
    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_stuff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_stuff') is not True:
            raise ValueError('Superuser must have is_stuff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        
        return self.create_user(username, password, **extra_fields)

class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='follower_set')
    following = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='following_set')

    objects = CustomUserManager()