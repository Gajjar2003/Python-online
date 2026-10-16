
from django.shortcuts import render
from myapp.models import *


def home(request):

    # Food Categories
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

    # Restaurants
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


    context = {
        "categories": categories,
        "restaurants": restaurants,
        "products": products,
    }

    return render(request, "home.html", context)
