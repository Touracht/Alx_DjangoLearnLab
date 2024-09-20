from django.urls import path
from .views import register_user, login_user, ProfileView

urlpatterns = [
    path('register/', register_user, name = 'register'),
    path('login/', login_user,name = 'login'),
    path('profile/', ProfileView.as_view(), name = 'profile')
]
