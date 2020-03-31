from django.urls import path
from .views import *
# from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [

    # path('login/', TokenObtainPairView.as_view() , name='login'),

    #  #  ----  registration urls ----  # 
    # path('register/', UserCreateAPIView.as_view(), name='register'),

    #  #  ---- coral API urls ----  # 
    # path('coraltype/', TypeListView.as_view(), name='type_list'),
    # path('coraltype/corals/', ItemListView.as_view(), name='item_list'),
    
    # #  ---- orders API urls ----  # 
    # path('orders/', OrdersListView.as_view(), name='new-order'),
    # path('orders/create', OrdersCreatView.as_view(), name='creat-order'),

]