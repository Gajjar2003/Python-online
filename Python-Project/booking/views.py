from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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

@login_required(login_url='user-login')
def book_now(request):

    return render(
        request,
        "book-now.html"
    )


# =====================================================
# MY BOOKING
# =====================================================

@login_required(login_url='user-login')
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
                    "err":
                    "Username already exists!"
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
                "meg":
                "User Created Successfully!"
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
        # STORE BOOKING DATA IN SESSION
        # =============================================

        request.session["booking_number"] = number

        request.session["booking_duration"] = duration

        request.session["booking_slot"] = slot_time

        request.session["booking_amount"] = amount


        # =============================================
        # OPEN PAYMENT PAGE
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
    # IF SESSION DATA NOT FOUND
    # =============================================

    if not slot_time:

        return redirect(
            "booking-form"
        )


    # =============================================
    # PAYMENT SUBMIT
    # =============================================

    if request.method == "POST":

        payment_method_value = request.POST.get(
            "payment_method"
        )


        # =========================================
        # CASH PAYMENT
        # =========================================

        if payment_method_value == "Cash":

            # Final slot check
            if Booking.objects.filter(
                slot_time=slot_time
            ).exists():

                request.session.flush()

                return redirect(
                    "booking-form"
                )


            Booking.objects.create(

                user=request.user,

                email=request.user.email,

                number=number,

                duration=duration,

                slot_time=slot_time,

                amount=amount,

                payment_method="Cash",

                payment_status="Pending"
            )


            # Clear session

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


        # =========================================
        # ONLINE PAYMENT
        # =========================================

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


    if not slot_time:

        return redirect(
            "booking-form"
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
    # CREATE PAID BOOKING
    # =============================================

    Booking.objects.create(

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


    return redirect(
        "my-booking"
    )