from django.db import models
from accounts.models import CustomUser
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Notification(models.Model):
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='notifications_receiver')
    actor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='notifications_sender')
    verb = models.CharField(max_length=50)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    target = GenericForeignKey('content_type', 'object_id')

    timestamp = models.DateTimeField(default=timezone.now)


