from rest_framework import permissions

class IsInstructor(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.is_instructor
