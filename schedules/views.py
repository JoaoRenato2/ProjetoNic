from django.contrib.auth import authenticate
from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from schedules.models import Usuario


# Create your views here.
def home(request):
    return render(request, 'LandingPages.html')


def Login(request):
    return render(request, 'Login_Register.html')


def Register(request):
    return render(request, 'Login_Register.html')


def validar_cadastro(request):

    nome = request.POST.get('username')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    user = Usuario.objects.filter(nome=nome)
        
    if len(nome.strip()) == 0 or len(senha.strip()) == 0:
        return HttpResponse('ola')
        
    if len(user) > 0:
        return redirect('Register.html/?status=1')
    try:
        user = Usuario(nome=nome, email=email, senha=senha)
        user.save()
        return redirect('/auth/cadastro/?status=0')
    except:
        return HttpResponse('/auth/Register.html/?status=4')
        
        
def validar_login(request):

    username = request.POST.get('username')
    senha = request.POST.get('senha')

    user_login = authenticate(username=username, password=senha)

    if user_login:
        return HttpResponse('ok')
    else:
        return HttpResponse('usuario ou senha invalidos')
    

        
