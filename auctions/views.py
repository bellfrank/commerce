from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib import messages



from .models import User, AuctionListings


def index(request):
    return render(request, "auctions/index.html")

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
        # take in the data the user submitted and save it as a form
        form = GeeksForm(request.POST)
        # check if the form data is valid
        if form.is_valid():
            # save the form data to model
            form.save()
            messages.success(request, 'Form submission successful')
            return HttpResponseRedirect(reverse("index"))

        else:
            # if the form is invalid then we re-render the page with the existing format
            return render(request, "auctions/create_listing.html", {
                "form": form
            })

    return render(request, "auctions/create_listing.html", {
            "form": GeeksForm()
        })

# class NewListingForm(forms.Form):
#     item_title = forms.CharField(max_length=64)
#     item_description = forms.CharField(max_length=64)
#     item_startbid = forms.DecimalField(max_digits=4, decimal_places=2)
#     item_url = forms.URLField(required=False)
#     item_category = forms.CharField(required=False)

class GeeksForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = AuctionListings
        fields = "__all__"