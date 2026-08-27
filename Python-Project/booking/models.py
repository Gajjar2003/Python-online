from django.db import models
from django.contrib.auth.models import User


class Booking(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    email = models.EmailField()

    number = models.CharField(
        max_length=15
    )

    booking_date = models.DateField()

    duration = models.CharField(
        max_length=50
    )

    slot_time = models.CharField(
        max_length=100
    )

    amount = models.IntegerField()

    payment_method = models.CharField(
        max_length=50
    )

    payment_status = models.CharField(
        max_length=50
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.booking_date} - {self.slot_time}"