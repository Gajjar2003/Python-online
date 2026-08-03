from django.contrib import admin
from  myapp.models import *

class Userview(admin.ModelAdmin):
    list_display = ('name','email','age','contact')

admin.site.register(Useradd,Userview)

# Register your models here.
