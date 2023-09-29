from django.shortcuts import render
from .models import Foods, Reservation, Orders
from django.db.models import Sum

# Create your views here.

# * Landing + Signin (Users)
# Landing page
def landing(request):
    return render(request, 'app_general/landing.html')

# Login page
def login(request):
    return render(request, 'app_general/login.html')

# Register page
def register(request):
    return render(request, 'app_general/register.html')

# * General 
# Home page if haven't login yet redirect to landing
def home(request):
    time = Orders.objects.filter(amount__isnull=True).aggregate(Sum('amount'))
    return render(request, 'app_general/home.html', time)

# Shop for customer to buy
def shop(request):
    return render(request, 'app_general/customer_page1.html')

# Cart page
def cart(request):
    return render(request, 'app_general/cart.html')

# History page
def history(request):
    return render(request, 'app_general/history.html')

# * Profile settings
# Main profile page
def profile(request):
    return render(request, 'app_general/profile.html')

# Edit profile
def editprofile(request):
    return render(request, 'app_genearal/editprofile.html')