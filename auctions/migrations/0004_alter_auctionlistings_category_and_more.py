# Generated by Django 4.0.2 on 2022-02-21 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_rename_item_startbid_auctionlistings_bid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlistings',
            name='category',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='auctionlistings',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
