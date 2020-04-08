from rest_framework.permissions import BasePermission

#  Models
from .models import *

# Serializers
from .serializers import *

class IsVender(BasePermission):
	message = "user have to be a Vender"

	def  has_permission(self, request, view):
		if request.user.is_staff or hasattr(request.user, 'vender'):
			return True
		return False


class CanCreateItem(BasePermission):
	message = "user have to be a AuctionOwner Vender"

	def has_permission(self, request, view):
		user_id = getattr(request.user, 'id')
		data =request.data['items']
		auction_id = data[0]['auction']
		if auction_id is not None:
			auction_obj = Auction.objects.get(id=auction_id)
			return user_id == auction_obj.vender.user.id
		return False

class IsAuctionOwner(BasePermission):
	message = "user have to be a AuctionOwner Vender"



	def has_object_permission(self, request, view, obj):
		if request.user.is_staff or (obj.vender.user == request.user):
			return True

		return False

class IsItemOwner(BasePermission):
	message = "user have to be a Item Owner"

	def has_object_permission(self, request, view, obj):
		if request.user.is_staff or (obj.auction.vender.user == request.user):
			return True

		return False

class IsVarifideBidder (BasePermission):                           
	message = "bidder have to provide a varified pyment info"

	def  has_permission(self, request, view):
		bidder_id = getattr(request.user.bidder, 'id')
		item_id =request.data['item']
		auction_obj=Item.objects.get(id=item_id).auction
		bidder_obj= Bidder.objects.get(id=bidder_id)
		Participant_Check=Participant.objects.filter(bidder=bidder_obj,auction=auction_obj).exists()
		if request.user.is_staff or Participant:
			return True
		return False

	