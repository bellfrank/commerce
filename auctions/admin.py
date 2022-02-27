from django.contrib import admin
from .models import AuctionListings, AuctionBids, Category

# Customizing Django app to show all aspects of listing

class AuctionListingAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "img", "category", "user", "last_modified")

class AuctionBidsAdmin(admin.ModelAdmin):
    list_display = ("amount", "user", "listing")

# Register your models here
admin.site.register(AuctionListings, AuctionListingAdmin)
admin.site.register(AuctionBids, AuctionBidsAdmin)
admin.site.register(Category)
