
from django.urls import path
from myapp.views import *

urlpatterns = [
    path("", user_register, name="user-register"),

    path("user-login/", user_login, name="user-login"),
    path("user-logout/", user_logout, name="user-logout"),

    path("home/", home, name="home"),

    path("search-product/", search_product, name="search-product"),

    path("add-to-cart/<int:product_id>/", add_to_cart, name="add-to-cart"),

    path("cart/", cart, name="cart"),

    path("update-cart/<int:product_id>/", update_cart, name="update-cart"),

    path("remove-cart/<int:product_id>/", remove_from_cart, name="remove-cart"),
]
