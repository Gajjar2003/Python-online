from django.db import models

# Create your models here.
class Student(models.Model):
  fname = models.CharField(max_length=50)
  lname = models.CharField(max_length=50)
  email = models.CharField(max_length=50)
  age  = models.IntegerField()
  subject =  models.CharField(max_length=50)
  marks = models.FloatField()
