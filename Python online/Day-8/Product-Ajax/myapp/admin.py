from django.contrib import admin
from myapp.models import *

class productinfromation(admin.ModelAdmin):
  list_display = ('name','qty','price')


admin.site.register(Prdouct,productinfromation)
# Register your models here.
