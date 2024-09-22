from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView, LikeView, UnlikeView, MarkNotificationAsReadView

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedView.as_view(), name = 'feed'),
    path('<int:pk>/like/', LikeView.as_view(), name = 'like'),
    path('<int:pk>/unlike/', UnlikeView.as_view(), name = 'unlike'),
    path('notifications/<int:pk>/read/', MarkNotificationAsReadView.as_view(), name='mark_notification_as_read'),
]
