from django.contrib import admin
from Simple_crud.myapp.models import *

class studentdiaply(admin.ModelAdmin):
    list_display = ('name','email','age')

admin.site.register(Student,studentdiaply)
