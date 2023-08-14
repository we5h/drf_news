from rest_framework import permissions


class IsAuthorAdminOrReadOnly(permissions.BasePermission):
    message = 'Changing of the content available only for the author.'

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return (
            obj.author == request.user
            or request.user.is_staff
            or request.method in permissions.SAFE_METHODS
        )