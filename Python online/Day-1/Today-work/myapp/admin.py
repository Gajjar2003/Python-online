from django.contrib import admin
from myapp.models import *

class productview(admin.ModelAdmin):
    list_display = ("name","qty","price")

admin.site.register(Product,productview)

# Register your models here.
