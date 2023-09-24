from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'app_general/home.html')

def customer(request):
    return render(request, 'app_general/customer_page1.html')