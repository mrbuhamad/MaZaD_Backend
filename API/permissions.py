from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
	message = "Please log in with the correct username"

	def has_object_permission(self, request, view, obj):
		if request.user.is_staff or (obj.user == request.user):
			return True

		return False