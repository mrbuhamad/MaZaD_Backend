from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [

    path('login/', TokenObtainPairView.as_view() , name='login'),

    #  #  ----  registration urls ----  # 
    path('register/', UserCreateAPIView.as_view(), name='register'),


    path('category/', CategoryView.as_view(), name='category'),

# ---  Auction urls   ----#
    path('auction/', AuctionListView.as_view(), name='auction'),
    path('auction/create', CreateAuctionView.as_view(), name='auction_create'),

# ---  item urls   ----#    
	path('auction/item', CreateItemView.as_view(), name='item_list'),
    path('item/create', CreateItemView.as_view(), name='item_create'),

  # ---  bid urls   ----#     
    path('auction/<int:item_id>/bid', BidListView.as_view(), name='bid'),
    path('item/bid/create', CreateBidView.as_view(), name='bid_create'),
    
    ]

    