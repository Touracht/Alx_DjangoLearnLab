from django.urls import path
from .views import register, login_view, LogOut, HomePageView, profile_management

urlpatterns = [
    path('home', HomePageView.as_view(), name = 'home'),
    path('register/', register, name = 'register'),
    path('login/', login_view, name = 'login'),
    path('logout/', LogOut.as_view(), name = 'logout'),
    path('profile/', profile_management, name = 'profile'),
]