from django.contrib import admin
from booking.models import *


class BookingAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "name",
        "email",
        "number",
        "slot_time",
        "duration",
        "booking_date",
        "price",
        "status",
        "created_at",
    )

    list_filter = (
        "duration",
        "status",
        "booking_date",
    )

    search_fields = (
        "name",
        "email",
        "number",
    )


admin.site.register(Booking,BookingAdmin)
