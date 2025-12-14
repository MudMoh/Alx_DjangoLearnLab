from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import PostViewSet, CommentViewSet, user_feed, like_post, unlike_post

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = router.urls + [
    path('feed/', user_feed, name='user_feed'),
    path('posts/<int:pk>/like/', like_post, name='like_post'),
    path('posts/<int:pk>/unlike/', unlike_post, name='unlike_post'),
]