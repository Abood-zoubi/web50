# Generated by Django 5.0.1 on 2024-01-26 13:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_comments_auction_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='auction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='auction_comment', to='auctions.auction'),
        ),
    ]
