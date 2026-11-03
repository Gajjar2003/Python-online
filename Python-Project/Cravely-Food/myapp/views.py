
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.conf import settings
from django.core.mail import send_mail
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.db import transaction
from django.views.decorators.http import require_POST
from django.urls import reverse
from django.contrib import messages
from datetime import datetime, time
from decimal import Decimal
import razorpay
import json
from django.db.models import Avg
from django.db import IntegrityError, transaction
from myapp.models import *


# ==========================================
# SEND ORDER CONFIRMATION EMAIL
# ==========================================

def send_order_email(order):

    try:

        items = order.items.select_related("product").all()


        subject = f"Cravely Order Confirmation #{order.id}"

        message = f"""
Hello {order.full_name},

Thank you for ordering from Cravely!

Your order has been successfully placed.

====================================
          ORDER DETAILS
====================================

Order ID: {order.id}

Customer Name: {order.full_name}

Registered Email: {order.email}

Mobile Number: {order.mobile}

Delivery Address:
{order.address}


====================================
          ORDER ITEMS
====================================
"""

        for item in items:

            item_total = item.price * item.quantity

            message += f"""

Product Name : {item.product.name}

Price        : Rs. {item.price}

Quantity     : {item.quantity}

Total        : Rs. {item_total}

------------------------------------
"""

        message += f"""

====================================
          PAYMENT DETAILS
====================================

Grand Total    : Rs. {order.total_amount}

Payment Method : {order.payment_method}

Payment Status : {order.payment_status}

Order Status   : {order.order_status}


Thank you for choosing Cravely!

Good Food. Great Mood.
"""

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [order.email],
            fail_silently=False
        )

        print("Order confirmation email sent successfully!")

        return True

    except Exception as e:

        print("Email sending failed:", e)

        return False


# ==========================================
# HOME PAGE
# ==========================================

@login_required(login_url="user-login")
def home(request):

    categories = [
        {"name": "Chinese", "icon": "🥡", "description": "Noodles & Manchurian"},
        {"name": "French Fries", "icon": "🍟", "description": "Crispy & golden"},
        {"name": "Coffee", "icon": "☕", "description": "Hot & refreshing"},
        {"name": "Drinks", "icon": "🥤", "description": "Cool & refreshing"},
        {"name": "Fast Food", "icon": "🍔", "description": "Quick tasty bites"},
        {"name": "Pizza", "icon": "🍕", "description": "Cheesy favourites"},
        {"name": "Biryani", "icon": "🍛", "description": "Rich & flavourful"},
        {"name": "Desserts", "icon": "🍰", "description": "Sweet treats"},
        {"name": "Sandwiches", "icon": "🥪", "description": "Fresh & delicious"},
        {"name": "Ice Cream", "icon": "🍨", "description": "Chilled happiness"},
        {"name": "Pasta", "icon": "🍝", "description": "Italian favourites"},
        {"name": "Momos", "icon": "🥟", "description": "Steamed & crispy"},
    ]

    restaurants = [
    {
        "name": "The Burger House",
        "cuisine": "Burgers, Fast Food",
        "rating": "4.8",
        "time": "20-30 min",
        "price": "₹199 for one",
        "image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=700&q=85",
        "tag": "BESTSELLER",
    },
    {
        "name": "Pizza District",
        "cuisine": "Italian, Pizza",
        "rating": "4.7",
        "time": "25-35 min",
        "price": "₹249 for one",
        "image": "https://images.unsplash.com/photo-1571407970349-bc81e7e96d47?auto=format&fit=crop&w=700&q=85",
        "tag": "POPULAR",
    },
    {
        "name": "Biryani Junction",
        "cuisine": "Biryani, North Indian",
        "rating": "4.6",
        "time": "25-40 min",
        "price": "₹179 for one",
        "image": "https://images.unsplash.com/photo-1633945274405-b6c8069047b0?auto=format&fit=crop&w=700&q=85",
        "tag": "MUST TRY",
    },
    {
        "name": "Chinese Wok",
        "cuisine": "Chinese, Noodles, Manchurian",
        "rating": "4.5",
        "time": "20-30 min",
        "price": "₹149 for one",
        "image": "https://images.unsplash.com/photo-1563245372-f21724e3856d?auto=format&fit=crop&w=700&q=85",
        "tag": "POPULAR",
    },
    {
        "name": "Royal Frankie Corner",
        "cuisine": "Frankie, Rolls, Street Food",
        "rating": "4.4",
        "time": "15-25 min",
        "price": "₹99 for one",
        "image": "https://images.unsplash.com/photo-1626700051175-6818013e1d4f?auto=format&fit=crop&w=700&q=85",
        "tag": "BESTSELLER",
    },
    {
        "name": "Coffee Culture",
        "cuisine": "Coffee, Beverages, Snacks",
        "rating": "4.7",
        "time": "15-25 min",
        "price": "₹129 for one",
        "image": "https://images.unsplash.com/photo-1509042239860-f550ce710b93?auto=format&fit=crop&w=700&q=85",
        "tag": "TRENDING",
    },
    {
        "name": "Sandwich Station",
        "cuisine": "Sandwiches, Fast Food",
        "rating": "4.5",
        "time": "20-30 min",
        "price": "₹119 for one",
        "image": "https://images.unsplash.com/photo-1528735602780-2552fd46c7af?auto=format&fit=crop&w=700&q=85",
        "tag": "POPULAR",
    },
    {
        "name": "Pasta Palace",
        "cuisine": "Italian, Pasta",
        "rating": "4.6",
        "time": "25-35 min",
        "price": "₹199 for one",
        "image": "https://images.unsplash.com/photo-1473093295043-cdd812d0e601?auto=format&fit=crop&w=700&q=85",
        "tag": "MUST TRY",
    },
 

    {
        "name": "South Spice Kitchen",
        "cuisine": "South Indian, Dosa, Idli",
        "rating": "4.7",
        "time": "20-30 min",
        "price": "₹129 for one",
        "image": "https://images.unsplash.com/photo-1589301760014-d929f3979dbc?auto=format&fit=crop&w=700&q=85",
        "tag": "MUST TRY",
    },
]

    products = Product.objects.filter(
        is_available=True
    ).order_by("name")

    cart_data = request.session.get("cart", {})

    cart_count = sum(cart_data.values())

    context = {
        "categories": categories,
        "restaurants": restaurants,
        "products": products,
        "cart_count": cart_count,
    }

    return render(request, "home.html", context)


# ==========================================
# USER REGISTER
# ==========================================

def user_register(request):

    if request.method == "POST":

        fname = request.POST.get("fname", "").strip()
        lname = request.POST.get("lname", "").strip()
        email = request.POST.get("email", "").strip()
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        if not fname or not email or not username or not password:

            return render(request, "user-register.html", {
                "err": "Please fill all required fields."
            })

        try:
            validate_email(email)
        except ValidationError:

            return render(request, "user-register.html", {
                "err": "Please enter a valid email."
            })

        if User.objects.filter(username=username).exists():

            return render(request, "user-register.html", {
                "err": "Username already exists!"
            })

        user = User.objects.create_user(
            first_name=fname,
            last_name=lname,
            email=email,
            username=username,
            password=password
        )

        return render(request, "user-register.html", {
            "meg": "User Register Successfully!"
        })

    return render(request, "user-register.html")


# ==========================================
# USER LOGIN
# ==========================================

def user_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("home")

        return render(request, "user-login.html", {
            "err": "Invalid Username and Password!"
        })

    return render(request, "user-login.html")


# ==========================================
# USER LOGOUT
# ==========================================

def user_logout(request):

    logout(request)

    return redirect("user-login")


# ==========================================
# SEARCH PRODUCT
# ==========================================

def search_product(request):

    query = request.GET.get("q", "").strip()

    products = Product.objects.filter(
        is_available=True
    )

    if query:

        products = products.filter(
            Q(name__icontains=query) |
            Q(category__icontains=query) |
            Q(description__icontains=query)
        )

    context = {
        "products": products,
        "query": query,
    }

    return render(request, "search_product.html", context)


# ==========================================
# ADD TO CART
# ==========================================

@login_required(login_url="user-login")
def add_to_cart(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id,
        is_available=True
    )

    cart = request.session.get("cart", {})

    product_id = str(product.id)

    cart[product_id] = cart.get(product_id, 0) + 1

    request.session["cart"] = cart
    request.session.modified = True

    cart_count = sum(cart.values())

    return JsonResponse({
        "success": True,
        "message": f"{product.name} added to cart successfully!",
        "cart_count": cart_count
    })


# ==========================================
# VIEW CART
# ==========================================

@login_required(login_url="user-login")
def cart(request):

    cart_data = request.session.get("cart", {})

    products = []

    grand_total = Decimal("0.00")

    for product_id, quantity in cart_data.items():

        product = Product.objects.filter(
            id=product_id,
            is_available=True
        ).first()

        if product and quantity > 0:

            total = product.price * quantity

            grand_total += total

            products.append({
                "product": product,
                "quantity": quantity,
                "total": total
            })

    cart_count = sum(cart_data.values())

    return render(request, "cart.html", {
        "products": products,
        "grand_total": grand_total,
        "cart_count": cart_count
    })


# ==========================================
# UPDATE CART
# ==========================================

@login_required(login_url="user-login")
def update_cart(request, product_id):

    if request.method == "POST":

        cart_data = request.session.get("cart", {})

        product_id = str(product_id)

        if product_id in cart_data:

            action = request.POST.get("action")

            if action == "increase":

                cart_data[product_id] += 1

            elif action == "decrease":

                cart_data[product_id] -= 1

                if cart_data[product_id] <= 0:
                    del cart_data[product_id]

        request.session["cart"] = cart_data
        request.session.modified = True

    return redirect("cart")


# ==========================================
# REMOVE FROM CART
# ==========================================

@login_required(login_url="user-login")
def remove_from_cart(request, product_id):

    if request.method == "POST":

        cart_data = request.session.get("cart", {})

        product_id = str(product_id)

        if product_id in cart_data:

            del cart_data[product_id]

        request.session["cart"] = cart_data
        request.session.modified = True

    return redirect("cart")


# ==========================================
# CHECKOUT PAGE
# ==========================================

@login_required(login_url="user-login")
def checkout(request):

    cart_data = request.session.get("cart", {})

    products = []

    grand_total = Decimal("0.00")

    for product_id, quantity in cart_data.items():

        product = Product.objects.filter(
            id=product_id,
            is_available=True
        ).first()

        if product and quantity > 0:

            total = product.price * quantity

            grand_total += total

            products.append({
                "product": product,
                "quantity": quantity,
                "total": total
            })

    if not products:
        return redirect("cart")

    # REGISTERED EMAIL
    registered_email = request.user.email.strip()

    if request.method == "POST":

        full_name = request.POST.get(
            "full_name", ""
        ).strip()

        mobile = request.POST.get(
            "mobile", ""
        ).strip()

        address = request.POST.get(
            "address", ""
        ).strip()

        payment_method = request.POST.get(
            "payment_method"
        )

        # VALIDATION

        if not full_name or not mobile or not address:

            return render(request, "checkout.html", {
                "products": products,
                "grand_total": grand_total,
                "error": "Please fill all delivery details."
            })

        if not registered_email:

            return render(request, "checkout.html", {
                "products": products,
                "grand_total": grand_total,
                "error": "Please add your registered email to your account."
            })

        try:

            validate_email(registered_email)

        except ValidationError:

            return render(request, "checkout.html", {
                "products": products,
                "grand_total": grand_total,
                "error": "Your registered email is invalid."
            })

        if not mobile.isdigit() or len(mobile) != 10:

            return render(request, "checkout.html", {
                "products": products,
                "grand_total": grand_total,
                "error": "Please enter a valid 10 digit mobile number."
            })

        if payment_method not in ["COD", "RAZORPAY"]:

            return redirect("checkout")

        # CREATE ORDER

        with transaction.atomic():

            order = Order.objects.create(

                user=request.user,

                full_name=full_name,

                email=registered_email,

                mobile=mobile,

                address=address,

                payment_method=payment_method,

                payment_status="Pending",

                order_status="Placed" if payment_method == "COD" else "Pending",

                total_amount=grand_total

            )

            for item in products:

                OrderItem.objects.create(

                    order=order,

                    product=item["product"],

                    quantity=item["quantity"],

                    price=item["product"].price

                )

        # CASH ON DELIVERY

        if payment_method == "COD":

            request.session["cart"] = {}
            request.session.modified = True

            # SEND EMAIL TO REGISTERED EMAIL

            send_order_email(order)

            return redirect(
                "order-success",
                order_id=order.id
            )

        # RAZORPAY ONLINE PAYMENT

        try:

            client = razorpay.Client(
                auth=(
                    settings.RAZORPAY_KEY_ID,
                    settings.RAZORPAY_KEY_SECRET
                )
            )

            payment_order = client.order.create({

                "amount": int(grand_total * 100),

                "currency": "INR",

                "receipt": f"order_{order.id}"

            })

            order.razorpay_order_id = payment_order["id"]

            order.save()

        except Exception as e:

            print("Razorpay Error:", e)

            order.delete()

            return render(request, "checkout.html", {
                "products": products,
                "grand_total": grand_total,
                "error": "Payment gateway error. Please try again."
            })

        return render(request, "checkout.html", {

            "products": products,

            "grand_total": grand_total,

            "order": order,

            "razorpay_order_id": payment_order["id"],

            "razorpay_amount": int(grand_total * 100),

            "razorpay_key": settings.RAZORPAY_KEY_ID,

            "payment_ready": True

        })

    return render(request, "checkout.html", {

        "products": products,

        "grand_total": grand_total

    })


# ==========================================
# VERIFY RAZORPAY PAYMENT
# ==========================================

@login_required(login_url="user-login")
@require_POST
def verify_payment(request):

    try:

        data = json.loads(request.body)

        order = Order.objects.get(
            id=data.get("order_id"),
            user=request.user
        )

        # PREVENT DUPLICATE EMAIL

        if order.payment_status == "Paid":

            return JsonResponse({
                "success": True,
                "redirect_url": reverse(
                    "order-success",
                    args=[order.id]
                )
            })

        razorpay_order_id = data.get("razorpay_order_id")

        razorpay_payment_id = data.get("razorpay_payment_id")

        razorpay_signature = data.get("razorpay_signature")

        if not all([
            razorpay_order_id,
            razorpay_payment_id,
            razorpay_signature
        ]):

            return JsonResponse({
                "success": False,
                "message": "Payment details are missing."
            }, status=400)

        if order.razorpay_order_id != razorpay_order_id:

            return JsonResponse({
                "success": False,
                "message": "Invalid payment order."
            }, status=400)

        client = razorpay.Client(
            auth=(
                settings.RAZORPAY_KEY_ID,
                settings.RAZORPAY_KEY_SECRET
            )
        )

        # VERIFY PAYMENT SIGNATURE

        client.utility.verify_payment_signature({

            "razorpay_order_id": razorpay_order_id,

            "razorpay_payment_id": razorpay_payment_id,

            "razorpay_signature": razorpay_signature

        })

        # UPDATE ORDER

        with transaction.atomic():

            order.payment_status = "Paid"

            order.order_status = "Placed"

            order.razorpay_payment_id = razorpay_payment_id

            order.razorpay_signature = razorpay_signature

            order.save()

            request.session["cart"] = {}
            request.session.modified = True

        # SEND EMAIL AFTER SUCCESSFUL PAYMENT

        send_order_email(order)

        return JsonResponse({
            "success": True,
            "redirect_url": reverse(
                "order-success",
                args=[order.id]
            )
        })

    except Order.DoesNotExist:

        return JsonResponse({
            "success": False,
            "message": "Order not found."
        }, status=404)

    except Exception as e:

        print("Payment Verification Error:", e)

        return JsonResponse({
            "success": False,
            "message": "Payment verification failed."
        }, status=400)


# ==========================================
# ORDER SUCCESS PAGE
# ==========================================

@login_required(login_url="user-login")
def order_success(request, order_id):

    order = get_object_or_404(
        Order,
        id=order_id,
        user=request.user
    )

    return redirect("home")

@login_required(login_url="user-login")
def my_order(request):

    orders = Order.objects.filter(
        user=request.user
    ).prefetch_related("items__product").order_by("-created_at")

    return render(request, "my-order.html", {
        "orders": orders
    })

# RESTAURANT TABLE BOOKING

@login_required(login_url="user-login")
def book_table(request):

    restaurant_name = request.GET.get(
        "restaurant",
        ""
    ).strip()

    if request.method == "POST":

        restaurant_name = request.POST.get(
            "restaurant_name",
            ""
        ).strip()

        booking_date = request.POST.get("booking_date")
        booking_time = request.POST.get("booking_time")
        session = request.POST.get("session")
        guests = request.POST.get("guests")

        try:
            selected_date = datetime.strptime(
                booking_date, "%Y-%m-%d"
            ).date()

            selected_time = datetime.strptime(
                booking_time, "%H:%M"
            ).time()

            guests = int(guests)

        except (ValueError, TypeError):
            messages.error(request, "Please enter valid booking details.")
            return redirect("book-table")

        today = datetime.now().date()

        if selected_date < today:
            messages.error(request, "Please select a valid future date.")
            return redirect("book-table")

        if guests < 1 or guests > 20:
            messages.error(request, "Guests must be between 1 and 20.")
            return redirect("book-table")

        # Allowed time checking

        valid_times = {
            "Morning": (time(10, 0), time(12, 0)),
            "Afternoon": (time(12, 0), time(16, 0)),
            "Evening": (time(16, 0), time(19, 0)),
            "Night": (time(19, 0), time(23, 0)),
        }

        if session not in valid_times:
            messages.error(request, "Invalid booking session.")
            return redirect("book-table")

        start_time, end_time = valid_times[session]

        if not (start_time <= selected_time < end_time):
            messages.error(request, "Selected time does not match the session.")
            return redirect("book-table")

        if selected_time.minute not in [0, 30]:
            messages.error(request, "Please select a valid 30-minute slot.")
            return redirect("book-table")

        try:
            with transaction.atomic():

                RestaurantBooking.objects.create(
                    user=request.user,
                    restaurant_name=restaurant_name,
                    booking_date=selected_date,
                    booking_time=selected_time,
                    session=session,
                    guests=guests
                )

            messages.success(
                request,
                "Your restaurant table has been booked successfully!"
            )

            return redirect("my-booking")

        except IntegrityError:

            messages.error(
                request,
                "Sorry! This time slot is already booked. Please select another time."
            )

    return render(request, "book_table.html", {
        "restaurant_name": restaurant_name
    })


# MY BOOKINGS

@login_required(login_url="user-login")
def my_booking(request):

    bookings = RestaurantBooking.objects.filter(
        user=request.user
    ).order_by("-created_at")

    return render(request, "my-booking.html", {
        "bookings": bookings
    })


# ==========================================
# PRODUCT REVIEW AND RATING
# ==========================================

@login_required(login_url="user-login")
def product_reviews(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    reviews = Review.objects.filter(
        product=product
    ).select_related("user")

    # CHECK EXISTING REVIEW

    existing_review = Review.objects.filter(
        user=request.user,
        product=product
    ).first()

    # CHECK DELIVERED ORDER

    purchased = OrderItem.objects.filter(
        order__user=request.user,
        order__order_status="Delivered",
        product=product
    ).exists()

    if request.method == "POST":

        rating = request.POST.get("rating")
        title = request.POST.get("title", "").strip()
        comment = request.POST.get("comment", "").strip()

        try:
            rating = int(rating)
        except (ValueError, TypeError):
            rating = 0

        if rating < 1 or rating > 5:

            messages.error(request, "Please select a valid rating.")

        elif not title or not comment:

            messages.error(request, "Please fill all review fields.")

        elif len(title) > 150:

            messages.error(request, "Review title is too long.")

        elif existing_review:

            # UPDATE EXISTING REVIEW

            existing_review.rating = rating
            existing_review.title = title
            existing_review.comment = comment

            existing_review.save()

            messages.success(
                request,
                "Your review has been updated successfully!"
            )

            return redirect(
                "product-reviews",
                product_id=product.id
            )

        elif not purchased:

            messages.error(
                request,
                "You can review this food only after your order is delivered."
            )

        else:

            # CREATE NEW REVIEW

            Review.objects.create(
                user=request.user,
                product=product,
                rating=rating,
                title=title,
                comment=comment
            )

            messages.success(
                request,
                "Your review has been submitted successfully!"
            )

            return redirect(
                "product-reviews",
                product_id=product.id
            )

    # AVERAGE RATING

    rating_data = reviews.aggregate(
        average=Avg("rating")
    )

    average_rating = rating_data["average"] or 0

    review_count = reviews.count()

    context = {
        "product": product,
        "reviews": reviews,
        "existing_review": existing_review,
        "purchased": purchased,
        "average_rating": average_rating,
        "review_count": review_count,
    }

    return render(
        request,
        "product_reviews.html",
        context
    )


# ==========================================
# DELETE PRODUCT REVIEW
# ==========================================

@login_required(login_url="user-login")
@require_POST
def delete_review(request, review_id):

    review = get_object_or_404(
        Review,
        id=review_id,
        user=request.user
    )

    product_id = review.product.id

    review.delete()

    messages.success(
        request,
        "Your review has been deleted successfully!"
    )

    return redirect(
        "product-reviews",
        product_id=product_id
    )