from rest_framework import permissions

class MessagePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in ["POST"] or request.user.is_superuser:
            return True
        else:
            return False