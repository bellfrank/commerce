# Generated by Django 4.0.2 on 2022-02-28 03:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_alter_auctionlistings_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctioncomments',
            name='body',
            field=models.TextField(default='none'),
        ),
        migrations.AddField(
            model_name='auctioncomments',
            name='name',
            field=models.CharField(default='none', max_length=255),
        ),
        migrations.AddField(
            model_name='auctionlistings',
            name='favorites',
            field=models.ManyToManyField(related_name='blog_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]