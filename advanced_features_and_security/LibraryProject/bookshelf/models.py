from django.db import models

class Book(models.Model):
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200)
    publication_year = models.IntegerField()

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, password):
        if not email:
            raise ValueError('The Email field must be set')
        user = self.model(email = self.normalize_email(email))
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(email, password)

        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=False)
    profile_photo = models.ImageField()

class Permissions(models.model):
    premissions = [('can_view', 'Can view'), ('can_create', 'Can view'),
                   ('can _edit', 'Can edit'), ('can_delete', 'Can delete')]