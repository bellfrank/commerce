
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib import messages
from django.core.mail import send_mail



from .models import User, AuctionListings, AuctionBids, AuctionComments, Category


def index(request):
    listings = AuctionListings.objects.all()
    
    bids = AuctionBids.objects.all()
    comments = AuctionComments.objects.all()
    
    return render(request, "auctions/index.html",{
        "listings": listings,
        "bids":bids,
        "comments": comments
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

    return render(request, "auctions/create_listing.html", {
            "form": GeeksForm()
        })

@login_required
def listing_page(request, listing_id):
    print("inside listing page views.py")
    listing_page = AuctionListings.objects.get(id=listing_id)
    print("Printing list page")
    
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        # request.FILES allows us to handle uploaded files with a model
        
        form = BidForm(request.POST)
        form.instance.user = AuctionListings.request.bid_user

        # check if the form data is valid
        if form.is_valid():
            # save the form data to model
            form.save()
            return HttpResponseRedirect(reverse("index"))

        else:
            # if the form is invalid then we re-render the page with the existing format
            return render(request, "auctions/listing.html", {
                "form": form
            })

    return render(request, "auctions/listing.html", {
            "form": BidForm()
        })

@login_required
def categories(request):
    category_choices = Category.objects.all().values_list('name','name')

    choice_list = []
    for item in category_choices:
        choice_list.append(item)
    
    return render(request, "auctions/categories.html", {
            "choice_list": choice_list
        })


@login_required
def categoryview(request, cats):
    category_posts = AuctionListings.objects.filter(category=cats)
    return render(request, "auctions/categoriesview.html", {
            "cats": cats.title(),
            "category_posts": category_posts
        })


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

#bid form

class BidForm(forms.ModelForm):
    class Meta:
        model = AuctionBids
        exclude = ['user', 'listing']