from rest_framework import permissions

class ReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS


class IsAuthenticated(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated


class IsSuperUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser

class IsOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS
   
    def has_object_permission(self, request, view, obj):
        if request.user:
            if request.user.is_superuser:
                return True
            else:
                return obj.owner == request.user
        else:
            return False