from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import date

# Models
from .models import *

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
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


class CreateItemSerializer(serializers.ModelSerializer):
    class  Meta:
        model= Item
        fields = ['name','start_price','image',"auction"]


class CreateBidSerializer(serializers.ModelSerializer):
    class  Meta:
        model= Bid
        fields = ['bid_price','item','bidder']

  