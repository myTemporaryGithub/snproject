from .serializers import UserSerializer, FriendRequestSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.decorators import action
from snapp.models import FriendRequest
from snapp.api.permissions import AdminPermission, ReviewerPermission, UserPermission


class UserViewSet(viewsets.ModelViewSet):
    """
    admin: can list, view, create, update, delete any user
    reviewer: can list, view any user
    user: can view, edit self
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [AdminPermission.__or__(ReviewerPermission)]
        elif self.action == 'retrieve':
            permission_classes = [
                AdminPermission.__or__(
                    ReviewerPermission.__or__(UserPermission)
                )
            ]
        elif self.action in ['update', 'partial_update']:
            permission_classes = [AdminPermission.__or__(UserPermission)]
        else:
            permission_classes = [AdminPermission]
        return [permission() for permission in permission_classes]


class FriendRequestViewSet(viewsets.ModelViewSet):
    """
    admin: can list, view, create, update, delete any request
    reviewer: can list, view any request
    user: can view requests for self, can update status
    TODO: partial update status by receiver
    """
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer


    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [AdminPermission.__or__(ReviewerPermission)]
        elif self.action == 'retrieve':
            permission_classes = [
                AdminPermission.__or__(
                    ReviewerPermission.__or__(UserPermission)
                )
            ]
        elif self.action in ['update', 'partial_update']:
            permission_classes = [AdminPermission.__or__(UserPermission)]
        else:
            permission_classes = [AdminPermission]
        return [permission() for permission in permission_classes]
