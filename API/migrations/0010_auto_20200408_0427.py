# Generated by Django 3.0.4 on 2020-04-08 01:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('API', '0009_auto_20200407_1719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='auction',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='pyment_type',
        ),
        migrations.AlterField(
            model_name='vender',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='vender', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='AuctionCharg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pyment_status', models.CharField(max_length=120)),
                ('pyment_Ip', models.CharField(max_length=120)),
                ('pyment_datetime', models.DateTimeField()),
                ('auction', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='API.Auction')),
                ('bidder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.Bidder')),
            ],
        ),
    ]
