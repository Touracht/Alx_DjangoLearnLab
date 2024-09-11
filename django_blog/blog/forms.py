from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, Post
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

custom_user = get_user_model()
class CustomUserUpdateForm(UserChangeForm):
    class Meta:
        model = custom_user
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()

    def clean_password(self):
        return self.initial.get('password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user', 'bio', 'image']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
    


