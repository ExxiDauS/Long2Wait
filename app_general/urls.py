from django.urls import include ,path
from . import views

# path('domain name/', function from views ex.views.function name, name)
urlpatterns = [
    path('', views.landing, name='landing'),
    path('home/', views.home, name='home'),
    path('customer/', views.shop, name='shop'),
]
