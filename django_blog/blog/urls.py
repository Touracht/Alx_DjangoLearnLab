from django.urls import path
from .views import register, login_view, HomePageView, profile_management, PostListView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView, CommentCreateView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('home', HomePageView.as_view(), name = 'home'),
    path('register/', register, name = 'register'),
    path('login/', login_view, name = 'login'),
    path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name = 'logout'),
    path('profile/', profile_management, name = 'profile'),
    path('posts/', PostListView.as_view(), name = 'posts'),
    path('post/new/', PostCreateView.as_view(), name = 'create_post'),
    path('post_detail/<int:pk>/', PostDetailView.as_view(), name = 'post_detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('posts/<int:post_id>/comments/new/', CommentCreateView.as_view(), name = 'comment_create'),
]