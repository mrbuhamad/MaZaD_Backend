from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.template import loader


# Create your models here.


class Addres(models.Model):
	country = models.CharField(max_length=120)
	area=models.CharField(max_length=120)
	block=models.CharField(max_length=120)
	street=models.CharField(max_length=120)
	house=models.CharField(max_length=120)
	user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)


	def __str__(self):
		return f"{self.area} {self.block} {self.street}"




class Bidder(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='bidder')

	def __str__(self):
		return self.user.username


class Vender(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='vender')

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
	category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
	start_date=models.DateTimeField()
	active = models.BooleanField (null=True)
	req_deposit=models.IntegerField(null=True,default=10)

	#----- below fields changes by signals----#
	started_at = models.DateTimeField(blank=True,null=True)
	ended_at=models.DateTimeField(blank=True,null=True)

	def __str__(self):
		return self.title




# bidder cannot bid if he didnt make a deposit
# link deposit to payment model (create a pyment model)



class Item(models.Model):
	name = models.CharField(max_length=120)
	start_price = models.DecimalField(max_digits=12, decimal_places=3)
	image = models.ImageField(null=True)
	created_on = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField (null=True)
	auction = models.ForeignKey(Auction, on_delete=models.CASCADE,null=True)


	def __str__(self):
		return self.name

	@property
	def display_start_price(self):
		return "%s KD" % self.price


class Payment(models.Model):
	Item = models.OneToOneField(Item, on_delete=models.CASCADE,null=True)
	bidder = models.ForeignKey(Bidder, on_delete=models.CASCADE,null=True)
	status=models.BooleanField(null=True)
	amount=models.DecimalField(max_digits=12, decimal_places=3,null=True)
	paymentToken=models.IntegerField(null=True)
	paymentId=models.CharField(max_length=120,null=True)
	paidOn=models.DateTimeField(null=True)


	def __str__(self):
		return self.bidder.user.username


class AuctionCharg(models.Model):
	auction = models.ForeignKey(Auction, on_delete=models.CASCADE,null=True)
	bidder = models.ForeignKey(Bidder, on_delete=models.CASCADE,null=True)
	status=models.BooleanField(null=True)
	amount=models.DecimalField(max_digits=12, decimal_places=3,null=True)
	paymentToken=models.IntegerField(null=True)
	paymentId=models.CharField(max_length=120,null=True)
	paidOn=models.DateTimeField(null=True)

	def __str__(self):
		return self.bidder.user.username

class Participant(models.Model):
	bidder= models.ForeignKey(Bidder, on_delete=models.CASCADE, related_name='participants')
	auction = models.ForeignKey(Auction, on_delete=models.CASCADE,null=True)

	def __str__(self):
		return self.bidder.user.username


class Bid(models.Model):
	bid_price = models.DecimalField(max_digits=12, decimal_places=3)
	created_on = models.DateTimeField(auto_now_add=True)
	item = models.ForeignKey(Item, on_delete=models.CASCADE,null=True)
	bidder = models.ForeignKey(Bidder, on_delete=models.CASCADE,null=True )
	
	#----- below fields changes by signals----#
	winner= models.BooleanField (default=False)

	def __str__(self):
		return f'{self.item} -- {self.bid_price}'

	@property
	def display_bid_price(self):
		return "%s KD" % self.price


#-------------- landing page modal  ------------- #
# 
class Clickes(models.Model):
	status= models.BooleanField (default=False)
	
	

class Subscribers(models.Model):
	email = models.EmailField(max_length=254)
	created_on = models.DateTimeField(auto_now_add=True,null=True,blank=True)

	def __str__(self):
		return self.email

class Question(models.Model):
	name = models.CharField(max_length=120)
	email = models.EmailField(max_length=254)
	message=models.TextField(null=True,blank=True)
	created_on = models.DateTimeField(auto_now_add=True,null=True,blank=True)



#-------------- singnel to populate Auction.started_at & ended_at  ------------- #

@receiver(pre_save, sender=Auction)
def get_started_at(instance, *args, **kwargs):
	if instance.active==True:
		instance.started_at=datetime.now()

@receiver(pre_save, sender=Auction)
def get_ended_at(instance, *args, **kwargs):
	if instance.active==False:
		instance.ended_at=datetime.now()


#-------------- singnel to populate participant model  ------------- #

@receiver(pre_save, sender=AuctionCharg)
def get_participant(instance, *args, **kwargs):
	if instance.status == True:
		Participant.objects.create(bidder=instance.bidder ,auction=instance.auction)

		

#-------------- singnel to populate winner bid  ------------- #
@receiver(pre_save, sender=Item)
def get_wining_bid(instance, *args, **kwargs):
	if instance.active==False:
		wining_bid=instance.bid_set.all().order_by('-bid_price')[0]
		wining_bid.winner=True
		wining_bid.save()


#  -----  Auto matic email sender to winner bid ---- #

@receiver(pre_save, sender=Bid)
def get_winner(instance, *args, **kwargs):
	if instance.winner==True:
		Bidder_Email=instance.bidder.user.email
		send_mail(
   		'Mazad.com bid pyment',
    	'congratulation you have won the bid :)',
   		settings.EMAIL_HOST_USER,
    	[Bidder_Email],
   		fail_silently=False,
)

# for our email we will be using google email :
# email: mazad.payment@gmail.com
# password: mazad2020
#


#-------------- singnel to delete part after auction end  ------------- #

@receiver(pre_save, sender=Auction)
def get_started_at(instance, *args, **kwargs):
	if instance.active==False:
		instance=Participant.objects.filter(auction=instance)
		instance.delete()




@receiver(post_save, sender=Question)
def get_Subscribers(instance,created, *args, **kwargs):
	if created:
		Bidder_Email=instance.email
		send_mail(
   		'Thank you from LiveMazad.co',
    	'Thank you for contacting  us. we will let you know of any new updates',
   		settings.EMAIL_HOST_USER,
    	[Bidder_Email],
   		fail_silently=False,
   		auth_user=None,
   		auth_password=None,
   		connection=None,
   		html_message=loader.render_to_string('index.html', {'name':instance.name})
)
