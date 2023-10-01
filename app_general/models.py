from django.db import models

# Create your models here.
#TODO: class Users(models.Model):

class Reservation(models.Model):
    total_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.ForeignKey("app_general.Orders", on_delete=models.SET_NULL, null=True)

class Foods(models.Model):
    foods_name = models.CharField(max_length=255)
    price = models.IntegerField()

class Orders(models.Model):
    foods = models.ForeignKey('app_general.Foods', on_delete=models.SET_NULL, null=True)
    queue = models.ForeignKey('app_general.Reservation', on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField()
    price = models.IntegerField()