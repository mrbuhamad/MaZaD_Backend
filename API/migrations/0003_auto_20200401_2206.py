# Generated by Django 3.0.4 on 2020-04-01 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_auto_20200401_0356'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='winner',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='auction',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.Category'),
        ),
        migrations.AlterField(
            model_name='auction',
            name='ended_at',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='auction',
            name='started_at',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='bid',
            name='bidder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.Bidder'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.Item'),
        ),
        migrations.AlterField(
            model_name='bidder',
            name='addres',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.Addres'),
        ),
        migrations.AlterField(
            model_name='item',
            name='active',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='auction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.Auction'),
        ),
        migrations.AlterField(
            model_name='vender',
            name='addres',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.Addres'),
        ),
    ]
