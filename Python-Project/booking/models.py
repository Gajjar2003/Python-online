from django.db import models
from django.contrib.auth.models import User


class Booking(models.Model):

    # Logged-in user
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    # User information
    username = models.CharField(
        max_length=150
    )

    email = models.EmailField()

    mobile = models.CharField(
        max_length=15
    )

    # Cricket slot
    slot_time = models.CharField(
        max_length=20
    )

    # Booking duration
    duration = models.IntegerField()

    # Total price
    price = models.IntegerField()

    # Booking created date/time
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return (
            f"{self.username} - "
            f"{self.slot_time} - "
            f"{self.duration} Hour"
        )