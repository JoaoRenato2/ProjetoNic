from django.http import request
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'LandingPages.html')


def Login_Register(request):
    return render(request, 'Login_Register.html')