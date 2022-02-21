from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

#listings 
class AuctionListings(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    bid = models.DecimalField(max_digits=4, decimal_places=2)
    url = models.URLField(blank=True)
    category = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return f"{self.id}: {self.title} {self.description} {self.bid}"
#bids


#comments