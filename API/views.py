from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,RetrieveUpdateAPIView,DestroyAPIView
from datetime import datetime

#  Models
from .models import *

# Serializers
from .serializers import *


# -----  user  views  ------#

class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer


class AddresCreateAPIView(CreateAPIView):
	serializer_class = AddresCreateSerializer

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

# -----  Categor  views  ------#

class CategoryView(ListAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer




# -----  Auction  views   ------#

class AuctionListView(ListAPIView):
	queryset = Auction.objects.filter(start_date__gte=datetime.now()).order_by('start_date')
	serializer_class = AuctionSerializer

class CreateAuctionView(CreateAPIView):
	serializer_class=CreateAuctionSerializer

	def perform_create(self, serializer):
		serializer.save(vender=self.request.user.vender)


class AuctionStatusView(RetrieveUpdateAPIView):
	queryset = Auction.objects.all()
	serializer_class = AuctionStatusSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'auction_id'


class AuctionUpdateView(RetrieveUpdateAPIView):
	queryset = Auction.objects.all()
	serializer_class = CreateAuctionSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'auction_id'

	def perform_update(self, serializer):
		serializer.save(vender=self.request.user.vender)


class DeleteAuctionView(DestroyAPIView):
	queryset = Auction.objects.all()
	serializer_class = AuctionSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'auction_id'

	def perform_delete(self, serializer):
		serializer.save(vender=self.request.user.vender)


class DepositCreateView(RetrieveUpdateAPIView):
	serializer_class = DepositUpdateSerializer
	
	def perform_create(self, serializer):
		serializer.save(bidder=self.request.user.bidder)


# -----  item  views   ------#

class ItemListView(RetrieveAPIView):
	queryset = Auction.objects.all()
	serializer_class = ItemListSerializer
	lookup_field="id"
	lookup_url_kwarg="auction_id"


class CreateItemView(CreateAPIView):
	serializer_class=CreateItemSerializer


class ItemStatusView(RetrieveUpdateAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemStatusSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'item_id'


class ItemUpdateView(RetrieveUpdateAPIView):
	queryset = Item.objects.all()
	serializer_class = CreateItemSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'item_id'


class DeleteItemView(DestroyAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'item_id'
	


# -----  bid  views   ------#

class BidListView(RetrieveAPIView):
	queryset = Item.objects.all()
	serializer_class = BidListSerializer
	lookup_field="id"
	lookup_url_kwarg="item_id"


class CreateBidView(CreateAPIView):
	serializer_class=CreateBidSerializer
	
	def perform_create(self, serializer):
		serializer.save(bidder=self.request.user.bidder)




	