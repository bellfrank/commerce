# Generated by Django 4.0.2 on 2022-03-03 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_rename_body_auctioncomments_add_comment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctioncomments',
            name='body',
            field=models.TextField(default='none'),
        ),
    ]