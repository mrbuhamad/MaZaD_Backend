from rest_framework.generics import CreateAPIView,ListAPIView
from .serializers import *

#  Models
from .models import *

# Serializers
from .serializers import *



class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer


# ---  Categor  views   ----#
class CategoryView(ListAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer


# ---  Categor  views   ----#
class AuctionListView(ListAPIView):
	queryset = Auction.objects.all()
	serializer_class = AuctionSerializer




	