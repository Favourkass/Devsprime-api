from rest_framework import permissions


class IsInstructor(permissions.BasePermission):
	def has_permission(self, request, view):
	# Course upload permissions are only allowed for instructors
		return request.user.is_instructor