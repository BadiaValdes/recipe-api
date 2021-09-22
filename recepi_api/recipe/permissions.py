# For object level permission
from rest_framework import permissions

# Custom Perm - Only the owner can modify the object
class IsOwnerOrReadOnly(permissions.BasePermission): 

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        print(request.META['REMOTE_ADDR'])
        return (obj.fk_user == request.user) or (request.user.is_staff)
        
class IsAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        print("PP")
        #print(request.META)
        isAdmin = False
        print(request.user.groups)
        if(request.user.is_staff):
            isAdmin = True

        return isAdmin
