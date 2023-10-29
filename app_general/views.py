from django.shortcuts import render
from .models import *
from app_general.forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse
from .forms import UserProfileForm, ExtendedProfileForm
from django.http import JsonResponse
import json

# Create your views here.

# * Landing + Signin (Users)
# Landing page
def landing(request):
    return render(request, 'app_general/nk_dev/landing.html')

# Login page
def login(request: HttpRequest):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request,user)
            return HttpResponseRedirect(reverse("home"))
        else:
            messages.success(request, "Username or Password is incorrect")
            return render(request, 'authenticate/login.html')
    else:
        return render(request, 'authenticate/login.html')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("landing"))

# Register page
def register(request: HttpRequest):
    # Post
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            customer = Customer.objects.get_or_create(user=user, name=user.username, email=user.email)
            auth_login(request, user)
            return HttpResponseRedirect(reverse("home"))
    else:
        form = RegisterForm()

    # Get
    context = {"form": form}
    return render(request, "app_general/register.html", context)

# Policy page
def policy(request):
    return render(request, 'app_general/policy.html')

# * General 
# Home page if haven't login yet redirect to landing
@login_required
def home(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Orders.objects.get_or_create(customer=customer, completed=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {'items': items, 'order': order}
    return render(request, 'app_general/tn_dev/home.html', context)

# Shop for customer to buy
def shop(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Orders.objects.get_or_create(customer=customer, completed=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    foods = Foods.objects.all()
    context = {'foods': foods, 'cartItems': cartItems}
    return render(request, 'app_general/shop.html', context)

# Cart page
@login_required
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Orders.objects.get_or_create(customer=customer, completed=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {'items': items, 'order': order}
    return render(request, 'app_general/cart.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print("Action: ", action)
    print("Product: ", productId)

    customer = request.user.customer
    product = Foods.objects.get(id=productId)
    order, created = Orders.objects.get_or_create(customer=customer, completed=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, foods=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    elif action == 'delete':
        orderItem.quantity = 0
    
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

def processOrder(request):
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Orders.objects.get_or_create(customer=customer, completed=False)
        total = int(data['total'])
        if total == order.get_cart_items:
            order.completed = True
            order.total_quantity = total
        order.save()
    print('Data:', data)
    return JsonResponse('Item checkout.', safe=False)

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
    