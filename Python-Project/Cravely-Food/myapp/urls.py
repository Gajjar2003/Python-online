
from django.urls import path
from myapp.views import *

urlpatterns = [

    # USER
    path("", user_register, name="user-register"),

    path("user-login/", user_login, name="user-login"),

    path("user-logout/", user_logout, name="user-logout"),

    # HOME
    path("home/", home, name="home"),

    # SEARCH
    path("search-product/", search_product, name="search-product"),

    # CART
    path(
        "add-to-cart/<int:product_id>/",
        add_to_cart,
        name="add-to-cart"
    ),

    path("cart/", cart, name="cart"),

    path(
        "update-cart/<int:product_id>/",
        update_cart,
        name="update-cart"
    ),

    path(
        "remove-cart/<int:product_id>/",
        remove_from_cart,
        name="remove-cart"
    ),

    # CHECKOUT
    path("checkout/", checkout, name="checkout"),

    # RAZORPAY PAYMENT VERIFICATION
    path(
        "verify-payment/",
        verify_payment,
        name="verify-payment"
    ),

    # ORDER SUCCESS
    path(
        "order-success/<int:order_id>/",
        order_success,
        name="order-success"
    ),

   path("my-order/", my_order, name="my-order"),

    path("book-table/", book_table, name="book-table"),

    path("my-booking/", my_booking, name="my-booking"),

    # PRODUCT REVIEWS

path(
    "product-reviews/<int:product_id>/",
    product_reviews,
    name="product-reviews"
),

path(
    "delete-review/<int:review_id>/",
    delete_review,
    name="delete-review"
),
]

