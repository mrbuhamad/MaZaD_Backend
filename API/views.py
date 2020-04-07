from rest_framework.generics import (
CreateAPIView,
ListAPIView,
RetrieveAPIView,
RetrieveUpdateAPIView,
DestroyAPIView)
from datetime import datetime

# permissions
from rest_framework.permissions import(
	AllowAny,
	IsAuthenticated)
from .permissions import *

#  Models
from .models import *

# Serializers
from .serializers import *


# -----  user  views  ------#

class UserCreateAPIView(CreateAPIView):
	permission_class= [AllowAny]
	serializer_class = UserCreateSerializer


class AddresCreateAPIView(CreateAPIView):
	serializer_class = AddresCreateSerializer
	permission_class= [IsAuthenticated]
	
	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

# -----  Categor  views  ------#

class CategoryView(ListAPIView):
	permission_class= [AllowAny]
	queryset = Category.objects.all()
	serializer_class = CategorySerializer




# -----  Auction  views   ------#

class AuctionListView(ListAPIView):
	permission_class= [AllowAny]
	queryset = Auction.objects.filter(start_date__gte=datetime.now()).order_by('start_date')
	serializer_class = AuctionSerializer
	


class CreateAuctionView(CreateAPIView):
	permission_classes= [IsVender]
	serializer_class=CreateAuctionSerializer

	def perform_create(self, serializer):
		serializer.save(vender=self.request.user.vender)



class AuctionStatusView(RetrieveUpdateAPIView):
	permission_class= [IsVender]
	queryset = Auction.objects.all()
	serializer_class = AuctionStatusSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'auction_id'


class AuctionUpdateView(RetrieveUpdateAPIView):
	permission_class= [IsVender]
	queryset = Auction.objects.all()
	serializer_class = CreateAuctionSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'auction_id'

	def perform_update(self, serializer):
		serializer.save(vender=self.request.user.vender)


class DeleteAuctionView(DestroyAPIView):
	permission_class= [IsVender]
	queryset = Auction.objects.all()
	serializer_class = AuctionSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'auction_id'

	def perform_delete(self, serializer):
		serializer.save(vender=self.request.user.vender)




# -----  item  views   ------#

class ItemListView(RetrieveAPIView):
	permission_class= [AllowAny]
	queryset = Auction.objects.all()
	serializer_class = ItemListSerializer
	lookup_field="id"
	lookup_url_kwarg="auction_id"


class CreateItemView(CreateAPIView):
	permission_class= [IsVender]
	serializer_class=CreateItemSerializer


class ItemStatusView(RetrieveUpdateAPIView):
	permission_class= [IsAuctionOwner]
	queryset = Item.objects.all()
	serializer_class = ItemStatusSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'item_id'


class ItemUpdateView(RetrieveUpdateAPIView):
	permission_class= [IsAuctionOwner]
	queryset = Item.objects.all()
	serializer_class = CreateItemSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'item_id'


class DeleteItemView(DestroyAPIView):
	permission_class= [IsAuctionOwner]
	queryset = Item.objects.all()
	serializer_class = ItemSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'item_id'
	


# -----  bid  views   ------#

class BidListView(RetrieveAPIView):
	permission_class= [AllowAny]
	queryset = Item.objects.all()
	serializer_class = BidListSerializer
	lookup_field="id"
	lookup_url_kwarg="item_id"


class CreateBidView(CreateAPIView):
	permission_class= [IsVarifideBidder]
	serializer_class=CreateBidSerializer
	
	def perform_create(self, serializer):
		serializer.save(bidder=self.request.user.bidder)



class PaymentCreateView(CreateAPIView):
	permission_class= [IsAuctionOwner]
	serializer_class= PaymentCreateSerializer



	