# Generated by Django 3.0.4 on 2020-06-15 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0012_clickes_subscribers'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribers',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
