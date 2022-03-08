
from signal import SIG_DFL
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib import messages
from django.core.mail import send_mail
from flask import render_template
from numpy import double



from .models import User, AuctionListings, AuctionBids, AuctionComments, Category


def index(request):
    listings = AuctionListings.objects.all()
    
    bids = AuctionBids.objects.all()
    comments = AuctionComments.objects.all()
    
    return render(request, "auctions/index.html",{
        "listings": listings,
        "bids":bids
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            messages.success(request, 'Form submission successful')
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def create_listing(request):
    # check if method is a post
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        # request.FILES allows us to handle uploaded files with a model
        form = GeeksForm(request.POST, request.FILES)
        form.instance.user = request.user

        # check if the form data is valid
        if form.is_valid():
            # save the form data to model
            form.save()
            return HttpResponseRedirect(reverse("index"))

        else:
            # if the form is invalid then we re-render the page with the existing format
            return render(request, "auctions/create_listing.html", {
                "form": form
            })
    else:
        return render(request, "auctions/create_listing.html", {
                "form": GeeksForm()
            })

@login_required
def close_listing(request, listing_id):
    # getting the objects for the specific page
    listing = AuctionListings.objects.get(id=listing_id)
    # setting status to false and saving 
    if listing.status:
        listing.status = False
    
    listing.save()

    return HttpResponseRedirect(reverse('listing_page', args=[str(listing_id)]))
    

def place_bid(request, listing_id):
    if request.method == "POST":
        pass





def listing_page(request, listing_id):
    listing = AuctionListings.objects.get(id=listing_id)

    # comments = AuctionComments.objects.get()
    watchlisted = False
    
    # check to see if AuctionListings.status is True else listing is closed
    status = listing.status

    # does the user have closing priveleges?
    close_privelege = False

    success_message = None
    

    # Check to see if the user seeing page is the person who posted the page
    if listing.user == request.user:
        close_privelege = True

    
    # checking databse to see if it's a favorited listing
    if listing.favorites.filter(id=request.user.id).exists():
        watchlisted = True

    

    if request.method == "POST":
        
        # retrieving Bid Form data
        form = BidForm(request.POST)
        form.instance.user = request.user
        form.instance.listing = listing

        bid = double(request.POST['amount'])

        if bid > listing.price:
            listing.price = bid
            # saving form and updating highest bid price on two models
            if form.is_valid():
                listing.save()
                form.save()
                success_message = "Bid Placed Succesfully!"
                # return HttpResponseRedirect(reverse('listing_page', args=[str(listing_id)]))
        else:
            success_message = "Bid must be higher than highest bid price."

    return render(request, "auctions/listing.html",{
        "listing": listing,
        "listing_form": CommentForm(),
        "bidform":BidForm(),
        "close_privelege":close_privelege,
        "listing_id":listing_id,
        "watchlisted":watchlisted,
        "status":status,
        "success_message":success_message,
    })


@login_required
def add_comment(request):
    pass

@login_required
def categories(request):
    category_choices = Category.objects.all()

    choice_list = []
    for item in category_choices:
        choice_list.append(item)
    
    return render(request, "auctions/categories.html", {
            "choice_list": choice_list
        })


@login_required
def categoryview(request, cats):
    category_posts = AuctionListings.objects.filter(category=cats)
    # comments_posts = AuctionComments.objects.filter(post=cats)
    return render(request, "auctions/categoriesview.html", {
            "cats": cats.title(),
            "category_posts": category_posts
        })


@login_required
def favorite_view(request, pk):
    # a different way of retrieving user submitted information
    post = get_object_or_404(AuctionListings, id=pk)
    favorited = False
    
    # checking to see if user favorited post
    if post.favorites.filter(id=request.user.id).exists():
        post.favorites.remove(request.user)
        favorited = False
    
    else:
        post.favorites.add(request.user)
        favorited = True

    return HttpResponseRedirect(reverse('listing_page', args=[str(pk)]))

@login_required
def watchlist(request):
    listings = AuctionListings.objects.filter(favorites=request.user)

    return render(request, "watchlist.html", {
        "listings":listings,
    })











# DJANGO FORMS ******************************************************************

class GeeksForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = AuctionListings
        fields = ('title', 'description','category', 'img', 'price')
        
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'})
        }

class BidForm(forms.ModelForm):
    class Meta:
        model = AuctionBids
        exclude = ['user', 'listing']

class CommentForm(forms.ModelForm):
    class Meta:
        model = AuctionComments
        exclude = ['post', 'name']
        widgets = {
            'add_comment': forms.Textarea(attrs={'class':'form-control'}),
        }