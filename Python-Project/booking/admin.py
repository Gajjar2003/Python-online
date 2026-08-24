from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = [
        "id",
        "user",
        "email",
        "number",
        "slot_time",
        "duration",
      
        "booking_date",
    ]

    list_filter = [
      
        "booking_date",
    ]

    search_fields = [
        "user__username",
        "email",
        "number",
        "slot_time",
    ]

    ordering = [
        "-booking_date"
    ]