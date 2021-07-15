# For object level permission
from rest_framework import permissions

# Custom Perm - Only the owner can modify the object
class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.fk_user == request.user