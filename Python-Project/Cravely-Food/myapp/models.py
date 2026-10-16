
from django.db import models


class Product(models.Model):
    CATEGORY_CHOICES = [
        ("Chinese", "Chinese"),
        ("French Fries", "French Fries"),
        ("Coffee", "Coffee"),
        ("Drinks", "Drinks"),
        ("Fast Food", "Fast Food"),
        ("Pizza", "Pizza"),
        ("Biryani", "Biryani"),
        ("Desserts", "Desserts"),
        ("Sandwiches", "Sandwiches"),
        ("Ice Cream", "Ice Cream"),
        ("Pasta", "Pasta"),
        ("Momos", "Momos"),
    ]

    name = models.CharField(max_length=150)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image_url = models.URLField(blank=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
