from django.urls import include ,path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('home/', views.home, name='home'),
    path('customer/', views.shop, name='shop'),
    # path('', include('django.contrib.auth.urls')),
]
