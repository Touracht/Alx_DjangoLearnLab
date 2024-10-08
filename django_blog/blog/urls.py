from django.urls import path
from .views import register, login_view, HomePageView, profile_management, PostListView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView, CommentCreateView, CommentUpdateView, CommentDeleteView, PostByTagListView, SearchView
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
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name = 'comment_create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='edit_comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete_comment'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='search_by_tag'),
    path('search/', SearchView.as_view(), name='search'),  
]