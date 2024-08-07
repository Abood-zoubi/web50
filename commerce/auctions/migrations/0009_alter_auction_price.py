# Generated by Django 5.0.1 on 2024-03-18 10:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_alter_auction_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='price',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='BidPrice', to='auctions.bid'),
        ),
    ]
