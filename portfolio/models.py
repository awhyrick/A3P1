from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import requests

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    cust_number = models.IntegerField(blank=False, null=False)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    email = models.EmailField(max_length=200)
    cell_phone = models.CharField(max_length=50)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.cust_number)


class Asset(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='assets')
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=timezone.now)
    created_date = models.DateTimeField(
        default=timezone.now)

    def created(self):
        self.date = timezone.now()
        self.save()

    def updated(self):
        self.date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.customer)

class Misc(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='miscs')
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now)
    created_date = models.DateTimeField(
        default=timezone.now)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.customer)




