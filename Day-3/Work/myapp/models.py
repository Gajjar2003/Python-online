from django.db import models

# Create your models here.

class Useradd(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    age = models.IntegerField()
    contact = models.IntegerField()
    image = models.ImageField(unique=True,default="j1.jpg")
    