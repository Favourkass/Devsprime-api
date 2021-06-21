from rest_framework import permissions


class CartOwner(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        return obj.learner_id.user_id == request.user
