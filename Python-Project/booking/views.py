from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings

from booking.models import Booking


# =====================================================
# HOME
# =====================================================

def index(request):
    return render(
        request,
        "index.html"
    )


# =====================================================
# BOOK NOW
# =====================================================

@login_required(login_url="user-login")
def book_now(request):

    return render(
        request,
        "book-now.html"
    )


# =====================================================
# MY BOOKING
# =====================================================

@login_required(login_url="user-login")
def my_booking(request):

    bookings = Booking.objects.filter(
        user=request.user
    ).order_by("-id")

    return render(
        request,
        "my-booking.html",
        {
            "bookings": bookings
        }
    )


# =====================================================
# ABOUT
# =====================================================

def about(request):

    return render(
        request,
        "about.html"
    )


# =====================================================
# SERVICE
# =====================================================

def service(request):

    return render(
        request,
        "service.html"
    )


# =====================================================
# REGISTER
# =====================================================

def user_register(request):

    if request.method == "POST":

        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(
            username=username
        ).exists():

            return render(
                request,
                "user-register.html",
                {
                    "err": "Username already exists!"
                }
            )

        User.objects.create_user(

            first_name=fname,
            last_name=lname,
            email=email,
            username=username,
            password=password
        )

        return render(
            request,
            "user-register.html",
            {
                "meg": "User Created Successfully!"
            }
        )

    return render(
        request,
        "user-register.html"
    )


# =====================================================
# LOGIN
# =====================================================

def user_login(request):

    if request.method == "POST":

        username = request.POST.get(
            "username"
        )

        password = request.POST.get(
            "password"
        )

        user = authenticate(
            username=username,
            password=password
        )

        if user is None:

            return render(
                request,
                "user-login.html",
                {
                    "err":
                    "Invalid Username and Password!"
                }
            )

        login(
            request,
            user
        )

        return redirect(
            "index"
        )

    return render(
        request,
        "user-login.html"
    )


# =====================================================
# LOGOUT
# =====================================================

def user_logout(request):

    logout(request)

    return redirect(
        "user-login"
    )


# =====================================================
# SEND BOOKING EMAIL
# =====================================================

def send_booking_email(
    booking,
    payment_status
):

    user = booking.user

    user_name = (
        user.get_full_name()
        or user.username
    )

    subject = "BoxCricket Booking Confirmation"

    message = f"""
Hello {user_name},

Your BoxCricket booking has been created successfully.

========================================
BOOKING DETAILS
========================================

Name        : {user_name}
Username    : {user.username}
Email       : {booking.email}
Mobile      : {booking.number}
Slot Time   : {booking.slot_time}
Duration    : {booking.duration}
Amount      : ₹{booking.amount}

Payment Method : {booking.payment_method}
Payment Status : {payment_status}

========================================

Thank you for booking with BoxCricket.

Regards,
BoxCricket Team
"""

    send_mail(

        subject,

        message,

        settings.DEFAULT_FROM_EMAIL,

        [booking.email],

        fail_silently=False
    )


# =====================================================
# BOOKING FORM
# =====================================================

@login_required(login_url="user-login")
def booking_form(request):

    if request.method == "POST":

        number = request.POST.get(
            "number"
        )

        duration = request.POST.get(
            "duration"
        )

        slot_time = request.POST.get(
            "slot_time"
        )

        # =============================================
        # CHECK SLOT
        # =============================================

        already_booked = Booking.objects.filter(
            slot_time=slot_time
        ).exists()

        if already_booked:

            return render(
                request,
                "booking-form.html",
                {
                    "err":
                    "This slot is already booked! Please select another slot.",

                    "selected_duration":
                    duration,

                    "selected_slot":
                    slot_time
                }
            )

        # =============================================
        # AMOUNT
        # =============================================

        amount = 0

        if duration == "1 Hour":

            amount = 700

        elif duration == "2 Hours":

            amount = 1200

        elif duration == "3 Hours":

            amount = 1800

        # =============================================
        # STORE DATA IN SESSION
        # =============================================

        request.session["booking_number"] = number

        request.session["booking_duration"] = duration

        request.session["booking_slot"] = slot_time

        request.session["booking_amount"] = amount

        # =============================================
        # PAYMENT PAGE
        # =============================================

        return redirect(
            "payment-method"
        )

    return render(
        request,
        "booking-form.html"
    )


# =====================================================
# PAYMENT METHOD
# =====================================================

@login_required(login_url="user-login")
def payment_method(request):

    number = request.session.get(
        "booking_number"
    )

    duration = request.session.get(
        "booking_duration"
    )

    slot_time = request.session.get(
        "booking_slot"
    )

    amount = request.session.get(
        "booking_amount"
    )

    # =============================================
    # SESSION CHECK
    # =============================================

    if not slot_time:

        return redirect(
            "booking-form"
        )

    # =============================================
    # CASH PAYMENT
    # =============================================

    if request.method == "POST":

        payment_method_value = request.POST.get(
            "payment_method"
        )

        if payment_method_value == "Cash":

            # Final slot check

            if Booking.objects.filter(
                slot_time=slot_time
            ).exists():

                return render(
                    request,
                    "booking-form.html",
                    {
                        "err":
                        "This slot is already booked! Please select another slot."
                    }
                )

            # =========================================
            # CREATE CASH BOOKING
            # =========================================

            booking = Booking.objects.create(

                user=request.user,

                email=request.user.email,

                number=number,

                duration=duration,

                slot_time=slot_time,

                amount=amount,

                payment_method="Cash",

                payment_status="Pending"
            )

            # =========================================
            # SEND CASH EMAIL
            # =========================================

            send_booking_email(
                booking,
                "Pending"
            )

            # =========================================
            # CLEAR SESSION
            # =========================================

            request.session.pop(
                "booking_number",
                None
            )

            request.session.pop(
                "booking_duration",
                None
            )

            request.session.pop(
                "booking_slot",
                None
            )

            request.session.pop(
                "booking_amount",
                None
            )

            return redirect(
                "my-booking"
            )

        # =============================================
        # ONLINE
        # =============================================

        elif payment_method_value == "Online":

            return render(
                request,
                "payment-method.html",
                {
                    "number": number,

                    "duration": duration,

                    "slot_time": slot_time,

                    "amount": amount,

                    "show_online": True
                }
            )

    # =============================================
    # PAYMENT PAGE
    # =============================================

    return render(
        request,
        "payment-method.html",
        {
            "number": number,

            "duration": duration,

            "slot_time": slot_time,

            "amount": amount
        }
    )


# =====================================================
# ONLINE PAYMENT DONE
# =====================================================

@login_required(login_url="user-login")
def online_payment_done(request):

    number = request.session.get(
        "booking_number"
    )

    duration = request.session.get(
        "booking_duration"
    )

    slot_time = request.session.get(
        "booking_slot"
    )

    amount = request.session.get(
        "booking_amount"
    )

    # =============================================
    # SESSION CHECK
    # =============================================

    if not slot_time:

        return redirect(
            "booking-form"
        )

    # =============================================
    # ONLY POST ALLOWED
    # =============================================

    if request.method != "POST":

        return redirect(
            "payment-method"
        )

    # =============================================
    # FINAL SLOT CHECK
    # =============================================

    if Booking.objects.filter(
        slot_time=slot_time
    ).exists():

        request.session.pop(
            "booking_number",
            None
        )

        request.session.pop(
            "booking_duration",
            None
        )

        request.session.pop(
            "booking_slot",
            None
        )

        request.session.pop(
            "booking_amount",
            None
        )

        return render(
            request,
            "booking-form.html",
            {
                "err":
                "This slot is already booked! Please select another slot."
            }
        )

    # =============================================
    # CREATE ONLINE PAID BOOKING
    # =============================================

    booking = Booking.objects.create(

        user=request.user,

        email=request.user.email,

        number=number,

        duration=duration,

        slot_time=slot_time,

        amount=amount,

        payment_method="Online",

        payment_status="Paid"
    )

    # =============================================
    # SEND SUCCESS EMAIL
    # =============================================

    send_booking_email(
        booking,
        "Paid"
    )

    # =============================================
    # CLEAR SESSION
    # =============================================

    request.session.pop(
        "booking_number",
        None
    )

    request.session.pop(
        "booking_duration",
        None
    )

    request.session.pop(
        "booking_slot",
        None
    )

    request.session.pop(
        "booking_amount",
        None
    )

    # =============================================
    # MY BOOKING
    # =============================================

    return redirect(
        "my-booking"
    )