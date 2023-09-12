from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
#TODO: build function to redirect
#TODO: Login system that identify who is host or customer
def home(request):
    return render(request, 'app_general/home.html')

def settings(request):
    return render(request, 'app_general/settings.html')