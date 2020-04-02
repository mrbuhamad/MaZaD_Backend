from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView
from datetime import datetime

#  Models
from .models import *

# Serializers
from .serializers import *



class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer


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

# -----  item  views   ------#

class ItemListView(RetrieveAPIView):
	queryset = Auction.objects.all()
	serializer_class = ItemListSerializer
	lookup_field="id"
	lookup_url_kwarg="auction_id"

class CreateItemView(CreateAPIView):
	serializer_class=CreateItemSerializer
	


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




	