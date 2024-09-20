from django.urls import path
from .views import register_user, login_user, ProfileView, FollowView, UnfollowView

urlpatterns = [
    path('register/', register_user, name = 'register'),
    path('login/', login_user,name = 'login'),
    path('profile/', ProfileView.as_view(), name = 'profile'),
    path('follow/<str:username>/', FollowView.as_view(), name = 'follow_user'),
    path('unfollow/<str:username>/', UnfollowView.as_view(), name = 'unfollow_user'),
]
