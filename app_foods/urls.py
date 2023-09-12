from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('<int:cart_id>', views.cart, name='cart')
]
