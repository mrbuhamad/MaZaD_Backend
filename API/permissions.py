from rest_framework.permissions import BasePermission

	

class IsVender(BasePermission):
	message = "user have to be a Vender"

	def has_object_permission(self, request, view, obj):
		if request.user.is_staff or obj.user.vender.exists():
			return True

		return False

class IsAuctionOwner(BasePermission):
	message = "user have to be a Vender"

	def has_object_permission(self, request, view, obj):
		if request.user.is_staff or (obj.user.vender == request.user.vender):
			return True

		return False


class IsVarifideBidder (BasePermission):
	message = "bidder have to provide a varified pyment info"

	def has_object_permission(self, request, view, obj):
		if request.user.is_staff or (obj.user == request.user):
			return True

		return False