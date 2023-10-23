from django.contrib import admin
from .models import *

# Register your models here.

# class FoodsAdmin(admin.ModelAdmin):
#     list_display = ['foods_name', 'price']
#     search_fields = ['foods_name']

admin.site.register(Foods)

# class OrdersAdmin(admin.ModelAdmin):
#     list_display = ['foods', 'queue', 'amount', 'price']
#     search_fields = ['foods']

admin.site.register(Orders)

# class ReservationAdmin(admin.ModelAdmin):
#     list_display = ['total_price', 'created_at', 'order']
#     search_fields = ['order']

admin.site.register(Reservation)

admin.site.register(Profile)

admin.site.register(OrderItem)