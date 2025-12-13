from rest_framework import serializers
from .models import Post, Comment, Like

class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'post', 'author', 'author_username', 'content', 'created_at', 'updated_at')
        read_only_fields = ('author', 'created_at', 'updated_at')

class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    comments_count = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'author', 'author_username', 'title', 'content', 'created_at', 'updated_at', 'comments', 'comments_count', 'likes_count', 'is_liked')
        read_only_fields = ('author', 'created_at', 'updated_at')

    def get_comments_count(self, obj):
        return obj.comments.count()

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_is_liked(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.likes.filter(user=request.user).exists()
        return False

class LikeSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Like
        fields = ('id', 'user', 'user_username', 'post', 'created_at')
        read_only_fields = ('user', 'created_at')
