from django.db import models
from django.contrib.auth.models import User


class Booking(models.Model):

    PAYMENT_CHOICES = [
        ("Cash", "Cash"),
        ("UPI", "UPI"),
        ("Card", "Card"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    email = models.EmailField()

    number = models.CharField(
        max_length=15
    )

    slot_time = models.CharField(
        max_length=100
    )

    duration = models.CharField(
        max_length=50
    )

    payment_option = models.CharField(
        max_length=20,
        choices=PAYMENT_CHOICES
    )

    booking_date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.slot_time}"