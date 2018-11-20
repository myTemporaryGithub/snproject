from rest_framework.permissions import BasePermission


class AdminPermission(BasePermission):
    """
    Admin permissions for viewsets
    """
    def has_permission(self, request, view):
        groups = list(request.user.groups.values_list('name', flat=True))
        if not groups:
            raise Exception(f'user group for user {request.user} not found')
        if 'admin' in groups:
            return True
        return False


class ReviewerPermission(BasePermission):
    """
    Reviewer permissions for viewsets
    """
    def has_permission(self, request, view):
        groups = list(request.user.groups.values_list('name', flat=True))
        if not groups:
            raise Exception(f'user group for user {request.user} not found')
        if 'reviewer' in groups:
            return True
        return False


class UserPermission(BasePermission):
    """
    User permissions for viewsets
    """
    def has_permission(self, request, view):
        groups = list(request.user.groups.values_list('name', flat=True))
        if not groups:
            raise Exception(f'user group for user {request.user} not found')
        if 'user' in groups:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if view.basename == 'friend-requests':
            return obj.sender == request.user or obj.receiver == request.user
        return obj == request.user
