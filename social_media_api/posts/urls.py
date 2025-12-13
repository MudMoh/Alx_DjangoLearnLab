from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import PostViewSet, CommentViewSet, user_feed

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = router.urls + [
    path('feed/', user_feed, name='user_feed'),
]