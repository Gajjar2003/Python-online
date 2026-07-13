from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    age = models.IntegerField()


class Coures(models.Model):
    Coures_titel = models.CharField(max_length=50)
    Coures_name = models.CharField(max_length=50)
    Coures_price = models.FloatField()