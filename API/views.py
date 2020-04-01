from rest_framework.generics import CreateAPIView,ListAPIView
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
		serializer.save(user=self.request.user)

# -----  item  views   ------#
class CreateItemView(CreateAPIView):
	serializer_class=CreateItemSerializer
	
	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

# -----  bid  views   ------#
class CreateBidView(CreateAPIView):
	serializer_class=CreateBidSerializer
	
	def perform_create(self, serializer):
		serializer.save(user=self.request.user)




	