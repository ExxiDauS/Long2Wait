from django.contrib import admin
from .models import *

# Register your models here.

class FoodsAdmin(admin.ModelAdmin):
    list_display = ['foods_name', 'price']
    search_fields = ['foods_name']

admin.site.register(Foods, FoodsAdmin)

class OrdersAdmin(admin.ModelAdmin):
    list_display = ['customer', 'date_ordered', 'completed', 'transaction_id', 'price']
    search_fields = ['customer']

admin.site.register(Orders)

class ReservationAdmin(admin.ModelAdmin):
    list_display = ['total_price', 'created_at', 'order']
    search_fields = ['order']

admin.site.register(Reservation)

admin.site.register(Profile)

admin.site.register(OrderItem)

admin.site.register(Customer)