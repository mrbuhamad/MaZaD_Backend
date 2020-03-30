# Generated by Django 3.0.4 on 2020-03-30 19:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid_price', models.DecimalField(decimal_places=3, max_digits=12)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categori',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('start_price', models.DecimalField(decimal_places=3, max_digits=12)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Vender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bidder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('start_date', models.DateTimeField()),
                ('active', models.BooleanField(null=True)),
                ('started_at', models.DateTimeField(null=True)),
                ('ended_at', models.DateTimeField(null=True)),
                ('categori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.Categori')),
                ('vender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.Vender')),
            ],
        ),
        migrations.CreateModel(
            name='Addres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=120)),
                ('area', models.CharField(max_length=120)),
                ('block', models.CharField(max_length=120)),
                ('street', models.CharField(max_length=120)),
                ('house', models.CharField(max_length=120)),
                ('bidder', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='API.Bidder')),
                ('vender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='API.Vender')),
            ],
        ),
    ]
