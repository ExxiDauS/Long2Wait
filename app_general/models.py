from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# User
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nickname = models.CharField(max_length=200, default="", null=True)

    def __str__(self):
        return self.nickname

class Reservation(models.Model):
    total_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.ForeignKey("app_general.Orders", on_delete=models.SET_NULL, null=True)

# Product
class Foods(models.Model):
    foods_name = models.CharField(max_length=100)
    price = models.IntegerField()
    # * image

    def __str__(self):
        return self.foods_name

# Order
class Orders(models.Model):
    # foods = models.ForeignKey('app_general.Foods', on_delete=models.SET_NULL, null=True)
    # queue = models.ForeignKey('app_general.Reservation', on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=200, null=True)
    amount = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return str(self.id)

# Cart
class OrderItem(models.Model):
    foods = models.ForeignKey(Foods, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Orders, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)