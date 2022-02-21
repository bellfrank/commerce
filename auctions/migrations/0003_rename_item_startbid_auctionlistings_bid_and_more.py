# Generated by Django 4.0.2 on 2022-02-11 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auctionlistings'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auctionlistings',
            old_name='item_startbid',
            new_name='bid',
        ),
        migrations.RenameField(
            model_name='auctionlistings',
            old_name='item_category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='auctionlistings',
            old_name='item_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='auctionlistings',
            old_name='item_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='auctionlistings',
            old_name='item_url',
            new_name='url',
        ),
    ]
