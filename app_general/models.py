from django.db import models

# Create your models here.
class Reservation(models.Model):
    total_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)