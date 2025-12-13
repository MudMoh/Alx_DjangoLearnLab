from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor_username = serializers.CharField(source='actor.username', read_only=True)
    target_description = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = ('id', 'actor', 'actor_username', 'verb', 'target_description', 'is_read', 'timestamp')
        read_only_fields = ('actor', 'timestamp')

    def get_target_description(self, obj):
        return str(obj.target)