from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def menu(request):
    return HttpResponse('menu')

def cart(request, cart_id):
    return HttpResponse('In cart ID = ' + str(cart_id))
