# Generated by Django 4.0.2 on 2022-03-02 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_alter_auctioncomments_body'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auctioncomments',
            old_name='body',
            new_name='add_comment',
        ),
        migrations.AlterField(
            model_name='auctionlistings',
            name='category',
            field=models.CharField(blank=True, choices=[('entertainment', 'entertainment'), ('sports', 'sports'), ('DNA', 'DNA'), ('motorcycles', 'motorcycles'), ('Other', 'Other')], max_length=64, null=True),
        ),
    ]
