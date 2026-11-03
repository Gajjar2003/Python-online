
from django.db import models


class Product(models.Model):
    CATEGORY_CHOICES = [
        ("Chinese", "Chinese"),
        ("French Fries", "French Fries"),
        ("Coffee", "Coffee"),
        ("Drinks", "Drinks"),
        ("Fast Food", "Fast Food"),
        ("Pizza", "Pizza"),
        ("Biryani", "Biryani"),
        ("Desserts", "Desserts"),
        ("Sandwiches", "Sandwiches"),
        ("Ice Cream", "Ice Cream"),
        ("Pasta", "Pasta"),
        ("Momos", "Momos"),
    ]

    name = models.CharField(max_length=150)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image_url = models.URLField(blank=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name



# ORDER MODEL

from django.contrib.auth.models import User


class Order(models.Model):

    PAYMENT_CHOICES = [
        ("COD", "Cash on Delivery"),
        ("RAZORPAY", "Razorpay"),
    ]

    PAYMENT_STATUS = [
        ("Pending", "Pending"),
        ("Paid", "Paid"),
        ("Failed", "Failed"),
    ]

    ORDER_STATUS = [
        ("Placed", "Placed"),
        ("Processing", "Processing"),
        ("Delivered", "Delivered"),
        ("Cancelled", "Cancelled"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    email = models.EmailField(blank=True, default="")
    full_name = models.CharField(max_length=150)
    mobile = models.CharField(max_length=15)
    address = models.TextField()

    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_CHOICES
    )

    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS,
        default="Pending"
    )

    order_status = models.CharField(
        max_length=20,
        choices=ORDER_STATUS,
        default="Placed"
    )

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    razorpay_order_id = models.CharField(
        max_length=100,
        blank=True
    )

    razorpay_payment_id = models.CharField(
        max_length=100,
        blank=True
    )

    razorpay_signature = models.CharField(
        max_length=255,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.user.username}"


# ORDER ITEM MODEL

class OrderItem(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items"
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT
    )

    quantity = models.PositiveIntegerField()

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    def __str__(self):
        return self.product.name

# RESTAURANT TABLE BOOKING MODEL

class RestaurantBooking(models.Model):

    SESSION_CHOICES = [
        ("Morning", "Morning"),
        ("Afternoon", "Afternoon"),
        ("Evening", "Evening"),
        ("Night", "Night"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    restaurant_name = models.CharField(max_length=150)

    booking_date = models.DateField()

    session = models.CharField(
        max_length=20,
        choices=SESSION_CHOICES
    )

    booking_time = models.TimeField()

    guests = models.PositiveIntegerField(default=2)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "restaurant_name",
                    "booking_date",
                    "booking_time"
                ],
                name="unique_restaurant_booking_slot"
            )
        ]

        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.restaurant_name} - {self.user.username}"


# ==========================================
# PRODUCT REVIEW MODEL
# ==========================================

class Review(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="product_reviews"
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="reviews"
    )

    rating = models.PositiveSmallIntegerField()

    title = models.CharField(max_length=150)

    comment = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

        constraints = [
            models.UniqueConstraint(
                fields=["user", "product"],
                name="unique_user_product_review"
            )
        ]

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"