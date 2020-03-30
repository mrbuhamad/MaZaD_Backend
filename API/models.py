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
