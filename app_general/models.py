from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Reservation(models.Model):
    total_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.ForeignKey("app_general.Orders", on_delete=models.SET_NULL, null=True)

class Foods(models.Model):
    foods_name = models.CharField(max_length=100)
    price = models.IntegerField()
    # def __str__(self) -> str:
    #     return '{} (id={})'.format(self.foods_name, self.id)

class Orders(models.Model):
    foods = models.ForeignKey('app_general.Foods', on_delete=models.SET_NULL, null=True)
    queue = models.ForeignKey('app_general.Reservation', on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField()
    price = models.IntegerField()

class Profile(models.Model):
    nickname = models.CharField(max_length=100, default="")
    user = models.OneToOneField(User, on_delete=models.CASCADE)