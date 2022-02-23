from django.contrib import admin
from .models import AuctionListings

# Customizing Django app to show all aspects of listing

class AuctionListingAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "url", "category", "user")
# Register your models here.
admin.site.register(AuctionListings, AuctionListingAdmin)

