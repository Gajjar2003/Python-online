
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from myapp.models import Product


# HOME PAGE
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


# USER REGISTER
def user_register(request):

    if request.method == "POST":

        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")

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


# USER LOGIN
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


# USER LOGOUT
def user_logout(request):

    logout(request)
    return redirect("user-login")


# SEARCH PRODUCT
def search_product(request):

    query = request.GET.get("q", "").strip()

    products = Product.objects.filter(is_available=True)

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



@login_required(login_url="user-login")

def add_to_cart(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    cart = request.session.get("cart", {})

    product_id = str(product.id)

    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1

    request.session["cart"] = cart
    request.session.modified = True

    cart_count = sum(cart.values())

    return JsonResponse({
        "success": True,
        "message": f"{product.name} added to cart successfully!",
        "cart_count": cart_count
    })



# VIEW CART
@login_required(login_url="user-login")
def cart(request):

    cart_data = request.session.get("cart", {})

    products = []
    grand_total = 0

    for product_id, quantity in cart_data.items():

        product = Product.objects.filter(id=product_id).first()

        if product:

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
