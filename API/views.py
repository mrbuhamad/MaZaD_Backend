from rest_framework.generics import CreateAPIView,ListAPIView
from datetime import datetime

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
	queryset = Auction.objects.filter(start_date__gte=datetime.now()).order_by('start_date')
	serializer_class = AuctionSerializer




	