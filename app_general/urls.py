from django.urls import include ,path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('customer/', views.shop, name='shop'),
    path("__reload__/", include("django_browser_reload.urls")),
]
