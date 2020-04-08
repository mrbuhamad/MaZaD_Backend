# Generated by Django 3.0.4 on 2020-04-08 22:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('API', '0010_auto_20200408_1629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctioncharg',
            name='pyment_Ip',
        ),
        migrations.RemoveField(
            model_name='auctioncharg',
            name='pyment_datetime',
        ),
        migrations.RemoveField(
            model_name='auctioncharg',
            name='pyment_status',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='pyment_Ip',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='pyment_datetime',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='pyment_status',
        ),
        migrations.AddField(
            model_name='auctioncharg',
            name='amount',
            field=models.DecimalField(decimal_places=3, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='auctioncharg',
            name='paidOn',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='auctioncharg',
            name='paymentId',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='auctioncharg',
            name='paymentToken',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='auctioncharg',
            name='status',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='amount',
            field=models.DecimalField(decimal_places=3, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='paidOn',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='paymentId',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='paymentToken',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='status',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='auctioncharg',
            name='bidder',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='API.Bidder'),
        ),
        migrations.AlterField(
            model_name='bidder',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bidder', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='participant',
            name='bidder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='API.Bidder'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='bidder',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='API.Bidder'),
        ),
    ]
