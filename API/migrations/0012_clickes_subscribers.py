# Generated by Django 3.0.4 on 2020-06-15 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0011_auto_20200409_0125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clickes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('email', models.CharField(max_length=120)),
            ],
        ),
    ]
