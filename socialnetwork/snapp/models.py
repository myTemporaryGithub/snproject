from django.db import models
from django.contrib.auth.models import User

class AbstractTrackedModel(models.Model):
    ctime = models.DateTimeField(auto_now_add=True, verbose_name='Creation time')
    mtime = models.DateTimeField(auto_now=True, verbose_name='Update time')

    class Meta:
        abstract = True

class FriendRequest(AbstractTrackedModel):

    STATUS_CHOICES = (
        (1, 'pending'),
        (2, 'confirmed'),
        (3, 'rejected'),
    )

    sender = models.ForeignKey(User, on_delete=models.PROTECT, related_name='friend_request_sender')
    receiver = models.ForeignKey(User, on_delete=models.PROTECT, related_name='friend_request_receiver')
    status = models.CharField(max_length=10, default=STATUS_CHOICES[0][0], choices=STATUS_CHOICES)

class Friend(AbstractTrackedModel):
    initiator = models.ForeignKey(User, on_delete=models.PROTECT, related_name='friend_initiator')
    friend = models.ForeignKey(User, on_delete=models.PROTECT, related_name='friend')

    class Meta:
        unique_together = (('initiator', 'friend'),)
