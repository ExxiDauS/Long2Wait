from django.contrib import admin
from app_general.models import Reservation, Foods, Orders

# Register your models here.

class FoodsAdmin(admin.ModelAdmin):
    list_display = ['foods_name', 'price']
    search_fields = ['foods_name']

admin.site.register(Foods, FoodsAdmin)

class OrdersAdmin(admin.ModelAdmin):
    list_display = ['foods', 'queue', 'amount', 'price']
    search_fields = ['foods']

admin.site.register(Orders, OrdersAdmin)

class ReservationAdmin(admin.ModelAdmin):
    list_display = ['total_price', 'created_at', 'order']
    search_fields = ['order']

admin.site.register(Reservation, ReservationAdmin)