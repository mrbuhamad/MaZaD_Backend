from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from datetime import date

# Models
from .models import *


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attr):
        data=super().validate(attr)
        token=self.get_token(self.user)
        data['user_id'] = self.user.id
        data['username'] = str(self.user)
        data['first_name'] = self.user.first_name
        data['last_name'] = self.user.last_name
        data['email'] = self.user.email
        if hasattr(self.user, 'vender'):
            data['is_vender'] = True
        else:
            data['is_vender'] = False
        return data


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    vender = serializers.BooleanField()
    class Meta:
        model = User
        fields = ['username','password','first_name','last_name','email','vender']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email=validated_data['email']
        vender=validated_data['vender']
        new_user = User(username=username,first_name=first_name,last_name=last_name,email=email)
        new_user.set_password(password)
        new_user.save()
        Bidder.objects.create(user=new_user)
        if vender==True:
            Vender.objects.create(user=new_user)
        return validated_data


class AddresCreateSerializer(serializers.ModelSerializer):
       class Meta:
        model = Addres
        exclude = ['user']



# ---  Category Serializers   ----#

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


# ---  Auction Serializers   ----#

class AuctionSerializer(serializers.ModelSerializer):
    user=serializers.SerializerMethodField()

    class Meta:
        model = Auction
        fields = ['id','title','description','start_date','active','req_deposit','started_at','ended_at','category','user']        

    def get_user(self,obj):
        print(User.objects.get(vender=obj.vender))
        user_obj=User.objects.get(vender=obj.vender)
        userId=user_obj.id
        return userId


class CreateAuctionSerializer(serializers.ModelSerializer):
    class  Meta:
        model= Auction
        fields = ['title','description','category','start_date',]



class AuctionStatusSerializer(serializers.ModelSerializer):
    class  Meta:
        model= Auction
        fields = ['active']




# ---  item Serializers   ----#

class ItemSerializer(serializers.ModelSerializer):
    class  Meta:
        model= Item
        fields = "__all__"



class ItemListSerializer(serializers.ModelSerializer):
    item_list=serializers.SerializerMethodField()

    class Meta:
        model = Auction
        fields = ["item_list"]

    def get_item_list(self,obj):
        item_list=Item.objects.filter(auction=obj.id)
        return ItemSerializer(item_list, many=True).data


class ItemsListSerializer(serializers.ModelSerializer):
    class  Meta:
        model= Item
        fields = ['name','start_price','image',"auction"]



class CreateItemSerializer(serializers.Serializer):
    items = ItemsListSerializer(many=True)

    def create(self, validated_data):
        Item_list = validated_data.get('items')
        for item in Item_list:
        	Item.objects.create(**item)
        return validated_data
      
     



class ItemStatusSerializer(serializers.ModelSerializer):
    class  Meta:
        model= Item
        fields = ['active']



# ---  bid Serializers   ----#

class BidSerializer(serializers.ModelSerializer):
    class  Meta:
        model= Bid
        fields = "__all__"



class BidListSerializer(serializers.ModelSerializer):
    bid_list=serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = ["bid_list"]

    def get_bid_list(self,obj):
        bid_list=Bid.objects.filter(item=obj.id)
        return BidSerializer(bid_list, many=True).data



class CreateBidSerializer(serializers.ModelSerializer):
    class  Meta:
        model= Bid
        fields = ['bid_price','item']




class PaymentCreateSerializer(serializers.ModelSerializer):
    class  Meta:
        model= Payment
        fields = "__all__"
  


class ChargCreateSerializer(serializers.ModelSerializer):
    class  Meta:
        model= AuctionCharg
        fields = "__all__"



# -----  landing page Serializers   ------#

class ClickesSerializer(serializers.ModelSerializer):
    class  Meta:
        model= Clickes
        fields = "__all__"


class SubscribersSerializer(serializers.ModelSerializer):
    class  Meta:
        model= Subscribers
        fields = "__all__"


class SubscribersListSerializer(serializers.Serializer):
    click_count=serializers.SerializerMethodField()
    Sub_count=serializers.SerializerMethodField()
    subscribers=serializers.SerializerMethodField()

    def get_subscribers(self,obj):
        subscribers=Subscribers.objects.all()
        return SubscribersSerializer(subscribers, many=True).data

    

    def get_click_count(self,obj):
        click=Clickes.objects.all().count()
        return click

    def get_Sub_count(self,obj):
        Sub=Subscribers.objects.all().count()
        return Sub

