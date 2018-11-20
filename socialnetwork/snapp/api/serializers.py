from rest_framework import serializers
from django.contrib.auth.models import User
from snapp.models import Friend, FriendRequest
from pprint import pprint


class UserSerializer(serializers.ModelSerializer):
    friend_list = serializers.SerializerMethodField()

    class Meta:
        model = User
        exclude = ('password',)

    def get_friend_list(self, user):
        initiated_by_user = list(Friend.objects.filter(initiator=user).values_list('friend__username', flat=True))
        initiated_by_friend = list(Friend.objects.filter(friend=user).values_list('initiator__username', flat=True))
        return initiated_by_user + initiated_by_friend


class FriendRequestSerializer(serializers.ModelSerializer):

    sender = serializers.PrimaryKeyRelatedField(read_only=True) 
    receiver = serializers.PrimaryKeyRelatedField(read_only=True) 

    class Meta:
        model = FriendRequest
        exclude = ()
