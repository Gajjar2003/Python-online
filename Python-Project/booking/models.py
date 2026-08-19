from django.db import models
from django.contrib.auth.models import User


class Booking(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=100)

    email = models.EmailField()

    number = models.CharField(max_length=15)

    slot_time = models.CharField(max_length=50)

    duration = models.CharField(max_length=20)

    booking_date = models.DateField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        default="Pending"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.name} - {self.slot_time}"