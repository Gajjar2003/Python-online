from django.db import models
from django.contrib.auth.models import User


class Booking(models.Model):

    PAYMENT_STATUS_CHOICES = [

        ("Pending", "Pending"),

        ("Paid", "Paid"),

    ]

    PAYMENT_METHOD_CHOICES = [

        ("Cash", "Cash"),

        ("Online", "Online"),

    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    email = models.EmailField()

    number = models.CharField(
        max_length=15
    )

    duration = models.CharField(
        max_length=50
    )

    slot_time = models.CharField(
        max_length=100
    )

    amount = models.IntegerField(
        default=0
    )

    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHOD_CHOICES,
        default="Cash"
    )

    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS_CHOICES,
        default="Pending"
    )

    booking_date = models.DateField(
        auto_now_add=True
    )

    def __str__(self):

        return f"{self.user.username} - {self.slot_time}"