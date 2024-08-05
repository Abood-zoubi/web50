# Generated by Django 5.0.1 on 2024-04-25 16:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0018_remove_bid_bidder_bid_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='bidder',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bidder_name', to=settings.AUTH_USER_MODEL),
        ),
    ]
