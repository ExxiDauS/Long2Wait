from django.urls import include ,path
from . import views

# path('domain name/', function from views ex.views.function name, name)
urlpatterns = [
    # * Authentication
    path('', views.landing, name='landing'),
    path('register/', views.register, name='register'),
    path('', include("django.contrib.auth.urls")),
    path('policy/', views.policy, name='policy'),

    # * General
    path('home/', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('cart/', views.cart, name='cart'),
    
    # * User
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', view=views.profile, name='profile'),

    path('update_item/', views.updateItem, name='update_item'),
]
