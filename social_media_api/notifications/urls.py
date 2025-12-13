from django.urls import path
from .views import NotificationListView, mark_notification_read

urlpatterns = [
    path('', NotificationListView.as_view(), name='notification_list'),
    path('<int:notification_id>/read/', mark_notification_read, name='mark_notification_read'),
]