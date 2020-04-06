# Generated by Django 3.0.4 on 2020-04-06 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0007_auto_20200406_1831'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pyment_status', models.CharField(max_length=120)),
                ('pyment_Ip', models.CharField(max_length=120)),
                ('pyment_datetime', models.DateTimeField()),
                ('Item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='API.Item')),
                ('bidder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.Bidder')),
            ],
        ),
        migrations.DeleteModel(
            name='Deposit',
        ),
    ]