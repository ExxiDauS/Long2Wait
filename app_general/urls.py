from django.urls import include ,path
from . import views

# path('domain name/', function from views ex.views.function name, name)
urlpatterns = [
    # * Authentication
    path('', views.landing, name='landing'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('', include("django.contrib.auth.urls")),
    path('policy/', views.policy, name='policy'),

    # * General
    path('home/', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.processOrder, name='processOrder'),
    
    # * User
    path('dashboard/', views.dashboard, name='dashboard'),

    path('update_item/', views.updateItem, name='update_item'),
]
