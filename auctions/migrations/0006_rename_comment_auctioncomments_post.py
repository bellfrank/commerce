# Generated by Django 4.0.2 on 2022-02-28 03:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auctioncomments_body_auctioncomments_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auctioncomments',
            old_name='comment',
            new_name='post',
        ),
    ]