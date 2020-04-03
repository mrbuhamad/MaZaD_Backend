from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [

    # #  -------------------  registration urls -------------------  # 
    path('login/', TokenObtainPairView.as_view() , name='login'),
    
    path('register/', UserCreateAPIView.as_view(), name='register'),


    # #  --------------------  category urls   ---------------------#

    path('category/', CategoryView.as_view(), name='category'),


    # #  --------------------  Auction urls   ---------------------#

    # Auction list shows all upcoming auction list from all venders
    path('auction/', AuctionListView.as_view(), name='auction'), 

    # auction create with the folowing requierd feild ['title','description','category','start_date',]
    # start_date should be formated as [2021-10-22T18:17:51]
    path('auction/create', CreateAuctionView.as_view(), name='auction_create'), 

    # auction update with the folowing requierd feild ['title','description','category','start_date',]
    # start_date should be formated as [2021-10-22T18:17:51]
    path('auction/<int:auction_id>/update', AuctionUpdateView.as_view(), name='auction_update'), 


 	# auction delete api
    path('auction/<int:auction_id>/delete', DeleteAuctionView.as_view(), name='auction_delete'), 


 	# URL for start/end auction butten update (active = True to start) update (active = False to end)
	path('auction/<int:auction_id>/status', AuctionStatusView.as_view(), name='auction_status'),
 
    # # --------------------  item urls   ---------------------#   

     # item list for a specific auction - put auction_id in the url  
	path('auction/<int:auction_id>/item', ItemListView.as_view(), name='item_list'),

    # item create with the folowing requierd feild ['name','start_price','image',"auction"]
    path('item/create', CreateItemView.as_view(), name='item_create'),

    # item update with the folowing requierd feild ['name','start_price','image',"auction"]
    path('item/<int:item_id>/update', ItemUpdateView.as_view(), name='item_update'),

	# auction item api
    path('item/<int:item_id>/delete', DeleteItemView.as_view(), name='item_delete'), 

    # URL for start/end Item auction butten update (active = True to start) update (active = False to end)
	path('item/<int:item_id>/status', ItemStatusView.as_view(), name='item_status'),


    # # --------------------  bid urls   ---------------------#    

    # bid list for a specific item - put item_id in the url  
    path('auction/<int:item_id>/bid', BidListView.as_view(), name='bid'),

    # bid create with the folowing requierd feild ['bid_price','item']
    path('item/bid/create', CreateBidView.as_view(), name='bid_create'),
    
    ]

    