# Generated by Django 3.0.4 on 2020-03-30 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_delete_auction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='item',
        ),
        migrations.RemoveField(
            model_name='bidder',
            name='addres',
        ),
        migrations.RemoveField(
            model_name='bidder',
            name='user',
        ),
        migrations.DeleteModel(
            name='Categori',
        ),
        migrations.RemoveField(
            model_name='vender',
            name='addres',
        ),
        migrations.RemoveField(
            model_name='vender',
            name='user',
        ),
        migrations.DeleteModel(
            name='Addres',
        ),
        migrations.DeleteModel(
            name='Bid',
        ),
        migrations.DeleteModel(
            name='Bidder',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='Vender',
        ),
    ]
