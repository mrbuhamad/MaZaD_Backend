from rest_framework.generics import (
CreateAPIView,
ListAPIView,
RetrieveAPIView,
RetrieveUpdateAPIView,
DestroyAPIView)
from datetime import datetime, timedelta
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response

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


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserCreateAPIView(CreateAPIView):
	permission_classes= [AllowAny]
	serializer_class = UserCreateSerializer


class AddresCreateAPIView(CreateAPIView):
	serializer_class = AddresCreateSerializer
	permission_classes= [IsAuthenticated]  
	
	def perform_create(self, serializer):
		serializer.save(user=self.request.user)


# -----  Categor  views  ------#

class CategoryView(ListAPIView):
	permission_classes= [AllowAny]
	queryset = Category.objects.all()
	serializer_class = CategorySerializer




# -----  Auction  views   ------#

class AuctionListView(ListAPIView):
	permission_classes= [AllowAny]
	queryset = Auction.objects.filter(start_date__gte=(datetime.now()-timedelta(hours=1))).order_by('start_date')
	serializer_class = AuctionSerializer
	


class CreateAuctionView(CreateAPIView):
	permission_classeses= [IsAuthenticated, IsVender]     # ------------------  works 
	serializer_class=CreateAuctionSerializer

	def perform_create(self, serializer):
		serializer.save(vender=self.request.user.vender)




class AuctionStatusView(RetrieveUpdateAPIView):
	permission_classes= [IsAuthenticated,IsVender,IsAuctionOwner]  # ------------------  works 
	queryset = Auction.objects.all() 
	serializer_class = AuctionStatusSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'auction_id'


class AuctionUpdateView(RetrieveUpdateAPIView):
	permission_classes= [IsAuthenticated,IsVender,IsAuctionOwner] # ------------------  works 
	queryset = Auction.objects.all()
	serializer_class = CreateAuctionSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'auction_id'

	def perform_update(self, serializer):
		serializer.save(vender=self.request.user.vender)


class DeleteAuctionView(DestroyAPIView):
	permission_classes= [IsAuthenticated,IsVender,IsAuctionOwner] # ------------------  works 
	queryset = Auction.objects.all()
	serializer_class = AuctionSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'auction_id'

	def perform_delete(self, serializer):
		serializer.save(vender=self.request.user.vender)




# -----  item  views   ------#

class ItemListView(RetrieveAPIView):
	permission_classes= [AllowAny]    # ------------------  works 
	queryset = Auction.objects.all()
	serializer_class = ItemListSerializer
	lookup_field="id"
	lookup_url_kwarg="auction_id"


class CreateItemView(CreateAPIView):
	permission_classes= [IsAuthenticated,IsVender,CanCreateItem] # ------------------  works
	serializer_class=CreateItemSerializer



class ItemStatusView(RetrieveUpdateAPIView): 
	permission_classes= [IsAuthenticated, IsVender,IsItemOwner] # ------------------  works
	queryset = Item.objects.all()
	serializer_class = ItemStatusSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'item_id'


class ItemUpdateView(RetrieveUpdateAPIView):
	permission_classes= [IsAuthenticated, IsVender,IsItemOwner] # ------------------  works
	queryset = Item.objects.all()
	serializer_class = CreateItemSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'item_id'


class DeleteItemView(DestroyAPIView):
	permission_classes= [IsAuthenticated, IsVender,IsItemOwner] # ------------------  works
	queryset = Item.objects.all()
	serializer_class = ItemSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'item_id'
	


# -----  bid  views   ------#

class BidListView(RetrieveAPIView):
	permission_classes= [AllowAny]
	queryset = Item.objects.all()
	serializer_class = BidListSerializer
	lookup_field="id"
	lookup_url_kwarg="item_id"


class CreateBidView(CreateAPIView):
	permission_classes= [IsAuthenticated, IsVarifideBidder]    # ------------------  works
	serializer_class=CreateBidSerializer
	
	def perform_create(self, serializer):
		serializer.save(bidder=self.request.user.bidder)



class PaymentCreateView(CreateAPIView):            
	permission_classes= [IsAuthenticated]   #----- what permissions do i need 
	serializer_class= PaymentCreateSerializer


class ChargCreateView(CreateAPIView):           
	permission_classes= [IsAuthenticated]    #----- what permissions do i need
	serializer_class= ChargCreateSerializer


# -----  landing page  views   ------#
	

class ClickesAPIView(CreateAPIView):
	permission_classes= [AllowAny]
	serializer_class = ClickesSerializer


class SubscribersAPIView(CreateAPIView):
	permission_classes= [AllowAny]
	serializer_class = SubscribersSerializer


class QuestionAPIView(CreateAPIView):
	permission_classes= [AllowAny]
	serializer_class = QuestionSerializer


class LandingPageView(APIView):
	def get(self, request):
		serializer = SubscribersListSerializer(self)
		return Response(serializer.data)


class QuestionListAPIView(ListAPIView):
	permission_classes= [AllowAny]
	queryset = Question.objects.all()
	serializer_class = QuestionSerializer
	




