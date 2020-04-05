from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import date

# Models
from .models import *

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    vender=vender=serializers.BooleanField()
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
        print(validated_data)
        return validated_data



# ---  Category Serializers   ----#

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'image', ]


# ---  Auction Serializers   ----#

class AuctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auction
        fields = "__all__"


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
        Item_list = validated_data.pop('items')
        for item in Item_list:
        	Item.objects.create(**item)
        return Item_list
      
     



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

#  what is many=true do ?   why do we add .data at the end



class CreateBidSerializer(serializers.ModelSerializer):
    class  Meta:
        model= Bid
        fields = ['bid_price','item']

  