from django.db import models

# Create your models here.
class AC_Services(models.Model):
    name= models.CharField(max_length=100)
    price= models.IntegerField()


class WM_Services(models.Model):
    name= models.CharField(max_length=100)
    price= models.IntegerField()

class RF_Services(models.Model):
    name= models.CharField(max_length=100)
    price= models.IntegerField()

class Users(models.Model):
    name= models.CharField(max_length=100)
    mobile= models.BigIntegerField()
    address=models.CharField(max_length=100)

