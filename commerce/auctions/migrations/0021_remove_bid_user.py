# Generated by Django 5.0.1 on 2024-05-02 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0020_alter_comments_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='user',
        ),
    ]