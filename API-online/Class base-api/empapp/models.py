from django.db import models


class dept(models.Model):
    name = models.CharField(max_length=100)
    hod = models.CharField(max_length=100)

class emp(models.Model):
    depts = models.ForeignKey(dept,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()