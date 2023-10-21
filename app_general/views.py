from django.shortcuts import render
from .models import Foods, Reservation, Orders
from app_general.forms import RegisterForm
from django.contrib.auth import login as auth_login
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

# * Landing + Signin (Users)
# Landing page
def landing(request):
    return render(request, 'app_general/nk_dev/landing.html')

# Login page
def login(request):
    return render(request, 'registration/login.html')

# Register page
def register(request: HttpRequest):
    # Post
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return HttpResponseRedirect(reverse("home"))
    else:
        form = RegisterForm()

    # Get
    context = {"form": form}
    return render(request, "app_general/register.html", context)

# * General 
# Home page if haven't login yet redirect to landing
def home(request):
    # time = Orders.objects.filter(amount__isnull=True).aggregate(Sum('amount'))
    return render(request, 'app_general/tn_dev/home.html')

# Shop for customer to buy
def shop(request):
    return render(request, 'app_general/customer_page1.html')

# Cart page
def cart(request):
    return render(request, 'app_general/cart.html')

# History page
def history(request):
    return render(request, 'app_general/history.html')

# * Dashboard settings
# Main profile page
def dashboard(request):
    return render(request, 'app_general/dashboard.html')

# Edit profile
def editprofile(request):
    return render(request, 'app_genearal/editprofile.html')