from django.contrib import admin
from .models import AuctionListings, AuctionBids, AuctionComments, User

# Customizing Django app to show all aspects of listing

class AuctionListingAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "img", "user", "last_modified", "price")
    # list_display = ("id", "title", "description", "img", "category", "user", "last_modified", "price")

class AuctionBidsAdmin(admin.ModelAdmin):
    list_display = ("amount", "user", "listing")

class AuctionListingComments(admin.ModelAdmin):
    list_display = ("post", "name", "body", "date_added")

# Register your models here
admin.site.register(AuctionListings, AuctionListingAdmin)
admin.site.register(AuctionBids, AuctionBidsAdmin)
# admin.site.register(Category)
admin.site.register(AuctionComments)
admin.site.register(User)
