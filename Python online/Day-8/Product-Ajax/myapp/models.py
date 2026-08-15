from django.db import models

# Create your models here.
class Prdouct(models.Model):
  name = models.CharField(max_length=50)
  qty = models.IntegerField()
  price = models.IntegerField()