from rest_framework import permissions


class IsAuthorAdminOrReadOnly(permissions.BasePermission):
    message = 'Changing of the content available only for the author/admin.'

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return (
            obj.author == request.user
            or request.user.is_staff
            or request.method in permissions.SAFE_METHODS
        )


class IsAuthorPostOwnerAdminOrReadOnly(IsAuthorAdminOrReadOnly):
    message = 'Comments deletion available for author of comment, post owner or admin only.'

    def has_object_permission(self, request, view, obj):
        return (
            obj.author == request.user
            or obj.post.author == request.user
            or request.user.is_staff
            or request.method in permissions.SAFE_METHODS
        )
