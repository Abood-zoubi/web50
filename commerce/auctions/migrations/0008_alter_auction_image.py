# Generated by Django 5.0.1 on 2024-01-29 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_auction_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='image',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
