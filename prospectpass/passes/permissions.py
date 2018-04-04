from rest_framework import permissions

class IsStudentOwner(permissions.BasePermission):
	def has_object_permission(self, request, view, student):
		if request.user:
			return student == request.user
		return False