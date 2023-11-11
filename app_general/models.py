from typing import Any
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# User
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nickname = models.CharField(max_length=200, default="", null=True)

    def __str__(self):
        return self.nickname

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, default="", null=True)
    email = models.CharField(max_length=200, default="", null=True)

    def __str__(self):
        return self.name

# Product
class Foods(models.Model):
    foods_name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.foods_name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

# Order
class Orders(models.Model):
    # foods = models.ForeignKey('app_general.Foods', on_delete=models.SET_NULL, null=True)
    # queue = models.ForeignKey('app_general.Reservation', on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=200, null=True)
    total_quantity = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return str(self.id)
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    
    @property
    def get_time(self):
        all_order = Orders.objects.all()
        time = sum([item.total_quantity for item in all_order]) * 5
        return time

# Cart
class OrderItem(models.Model):
    foods = models.ForeignKey(Foods, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Orders, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
    
    @property
    def get_total(self):
        total = self.foods.price * self.quantity
        return total

# Reservation
class Reservation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Orders, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return str(self.id)