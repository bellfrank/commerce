from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("listing/<int:listing_id>", views.listing_page, name="listing_page"),
    path("categories", views.categories, name="categories"),
    path("category/<str:cats>/", views.categoryview, name="category"),
    path("favorite/<int:pk>", views.favorite_view, name="favorite_post"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("close/<int:listing_id>", views.close_listing, name="close_listing"),
]
