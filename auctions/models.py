from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

#listings 
class AuctionListings(models.Model):
    user = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    last_modified = models.DateTimeField(auto_now_add = True)

    url = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return f"{self.id}: {self.title} {self.description} {self.url} {self.category}"

#bids
class AuctionBids(models.Model):
    bid = models.DecimalField(max_digits=4, decimal_places=0)
    total_bids = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.bid} {self.total_bids}"


#comments
class AuctionComments(models.Model):
    # comment = models.CharField(max_length=500, blank=True)
    comment = models.ForeignKey(AuctionListings, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"{self.id}: {self.comment}"
