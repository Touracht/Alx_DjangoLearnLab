from django.urls import path
from .views import register_user, login_user, ProfileView, FollowView, UnfollowView

urlpatterns = [
    path('register/', register_user, name = 'register'),
    path('login/', login_user,name = 'login'),
    path('profile/', ProfileView.as_view(), name = 'profile'),
    path('follow/<int:user_id>/', FollowView.as_view(), name = 'follow_user'),
    path('unfollow/<int:user_id>/', UnfollowView.as_view(), name = 'unfollow_user'),
]
