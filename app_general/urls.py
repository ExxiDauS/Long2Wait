from django.urls import include ,path
from . import views

# path('domain name/', function from views ex.views.function name, name)
urlpatterns = [
    path('', views.landing, name='landing'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('customer/', views.shop, name='shop'),
    path('', include("django.contrib.auth.urls")),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', view=views.profile, name='profile'),
]
