from django.db import models

# Create your models here.

class Bidder(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name


class Vender(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name


class Addres(models.Model):
    country = models.CharField(max_length=120)
    area=models.CharField(max_length=120)
    block=models.CharField(max_length=120)
    street=models.CharField(max_length=120)
    house=models.CharField(max_length=120)
    bidder = models.ForeignKey(Bidder, on_delete=models.CASCADE,null=True)
    vender = models.ForeignKey(Vender, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f"{self.area} {self.block} {self.street}"


class Categori(models.Model):
    type = models.CharField(max_length=120)

    def __str__(self):
        return self.type

class Auction(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    vender = models.ForeignKey(Vender, on_delete=models.CASCADE)
    categori = models.ForeignKey(Categori, on_delete=models.CASCADE)
    start_date=models.DateTimeField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField (Default=false)

    def __str__(self):
        return self.title


class Item(models.Model):
    name = models.CharField(max_length=120)
    start_price = models.DecimalField(max_digits=12, decimal_places=3)
	image = models.ImageField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField (Default=false)

    def __str__(self):
        return self.name

    @property
	def display_start_price(self):
		return "%s KD" % self.price



class Bid(models.Model):
    bid_price = models.DecimalField(max_digits=12, decimal_places=3)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
	def display_bid_price(self):
		return "%s KD" % self.price
