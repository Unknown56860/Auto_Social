from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def register_page(request):
    return render(request, 'users/register.html')

def login_page(request):
    return render(request, 'users/login.html')

def logout_page(request):
    return HttpResponse("Logout will be added soon...")
