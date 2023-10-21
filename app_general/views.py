from django.shortcuts import render
from .models import Foods, Reservation, Orders
from app_general.forms import RegisterForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse
from .forms import UserProfileForm, ExtendedProfileForm

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
@login_required
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
@login_required
def dashboard(request: HttpRequest):
    return render(request, 'app_general/dashboard.html')

# Edit profile
@login_required
def profile(request: HttpRequest):
    user = request.user

    # Post
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=user)
        is_new_profile = False
        
        try:
            # Updeate profile
            extended_profile = ExtendedProfileForm(request.POST, instance=user.profile)
        except:
            # Create new profile
            extended_profile = ExtendedProfileForm(request.POST)
            is_new_profile = True

        if form.is_valid() and extended_profile.is_valid():
            form.save()
            if is_new_profile:
                # Create new profile
                profile = extended_profile.save(commit=False)
                profile.user = user
                profile.save()
            else:
                # Update profile
                extended_profile.save()
            return HttpResponseRedirect(reverse("profile"))
    else:
        form = UserProfileForm(instance=user)
        try:
            extended_profile = ExtendedProfileForm(instance=user.profile)
        except:
            extended_profile = ExtendedProfileForm()

    # Get
    context = {
        "form": form,
        "extended_profile": extended_profile
    }
    return render(request, 'app_genearal/profile.html', context)