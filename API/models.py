from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.


class Addres(models.Model):
	country = models.CharField(max_length=120)
	area=models.CharField(max_length=120)
	block=models.CharField(max_length=120)
	street=models.CharField(max_length=120)
	house=models.CharField(max_length=120)


	def __str__(self):
		return f"{self.area} {self.block} {self.street}"




class Bidder(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	addres= models.ForeignKey(Addres, on_delete=models.CASCADE,default=1)

	def __str__(self):
		return self.user.username


class Vender(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	addres= models.ForeignKey(Addres, on_delete=models.CASCADE,default=1)

	def __str__(self):
		return self.user.username




class Category(models.Model):
	name = models.CharField(max_length=120)
	image = models.ImageField(blank=True)
	def __str__(self):
		return self.name



class Auction(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField()
	vender = models.ForeignKey(Vender, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	start_date=models.DateTimeField()
	active = models.BooleanField (null=True)

	#----- below fields changes by signals----#
	started_at = models.DateTimeField(null=True)
	ended_at=models.DateTimeField(null=True)

	def __str__(self):
		return self.title


class Item(models.Model):
	name = models.CharField(max_length=120)
	start_price = models.DecimalField(max_digits=12, decimal_places=3)
	image = models.ImageField(null=True)
	created_on = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField (default=False)
	auction = models.ForeignKey(Auction, on_delete=models.CASCADE)


	def __str__(self):
		return self.name

	@property
	def display_start_price(self):
		return "%s KD" % self.price



class Bid(models.Model):
	bid_price = models.DecimalField(max_digits=12, decimal_places=3)
	created_on = models.DateTimeField(auto_now_add=True)
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	def __str__(self):
		return self.name

	@property
	def display_bid_price(self):
		return "%s KD" % self.price




#-------------- singnel to populate Auction.started_at & ended_at  ------------- #
@receiver(pre_save, sender=Auction)
def get_started_at(instance, *args, **kwargs):
	if instance.active==True:
		instance.started_at=datetime.now()

@receiver(pre_save, sender=Auction)
def get_ended_at(instance, *args, **kwargs):
	if instance.active==False:
		instance.ended_at=datetime.now()
