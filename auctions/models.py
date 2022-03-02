from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

# category_choices = [('coding','coding'),('sports', 'sports'),('entertainment','entertainment')]

category_choices = Category.objects.all().values_list('name','name')

choice_list = []
for item in category_choices:
    choice_list.append(item)

class AuctionListings(models.Model):
    # make our user foreign key so if user deletes account, his posts get removed as well :) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    favorites = models.ManyToManyField(User, related_name='blog_posts')

    title = models.CharField(max_length=64)
    description = models.TextField(max_length=64)
    last_modified = models.DateField(auto_now_add = True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    # = models.URLField(blank=True, null=True)
    img = models.ImageField(upload_to='images/')

    category = models.CharField(max_length=64, blank=True, null=True, choices=choice_list)

    def __str__(self):
        return f"{self.id}: {self.title} {self.description} {self.url} {self.category}"

#bids
class AuctionBids(models.Model):
    # bid amount (to log the price)
    amount = models.DecimalField(max_digits=6, decimal_places=2, blank=False)

    # user(to log the user)
    user = models.ForeignKey(AuctionListings, on_delete=models.CASCADE, related_name="bid_user", blank=False)

    # listing(to log the listing it belongs to)
    listing = models.ForeignKey(AuctionListings, on_delete=models.CASCADE, related_name="bid_listing", blank=False)

    def __str__(self):
        return f"{self.id}: {self.amount} {self.user} {self.listing}"

#comments
class AuctionComments(models.Model):
    # comment = models.CharField(max_length=500, blank=True)
    post = models.ForeignKey(AuctionListings, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=255, default="none")
    body = models.TextField(default="none")
    # date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.id}: {self.post.title} {self.name} "
