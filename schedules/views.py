from hashlib import sha256

from django.contrib.auth import authenticate
from django.http import HttpResponse, request
from django.shortcuts import redirect, render
from django.contrib import messages

from schedules.models import Usuario


# Create your views here.
def home(request):
    return render(request, 'LandingPages.html')


def Login(request):
    status = request.GET.get('status')
    return render(request, 'Login_Register.html', {'status': status})


def Register(request):
    return render(request, 'Login_Register.html')


def validar_cadastro(request):

    nome = request.POST.get('username')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    user = Usuario.objects.filter(nome=nome)

    if len(nome.strip()) == 0 or len(senha.strip()) == 0:
        return redirect('/auth/cadastro/?status=1')

    if len(user) > 0:
        return redirect('/auth/cadastro/?status=2')
    try:
        senha = sha256(senha.encode()).hexdigest()
        user = Usuario(nome=nome, email=email, senha=senha)
        user.save()
        return redirect('/auth/index')
    except:
        return redirect('/auth/cadastro/?status=3')


def validar_login(request):

    username = request.POST.get('username')
    senha = request.POST.get('senha')

    user_login = authenticate(username=username, password=senha)

    if user_login:
        return render(request, 'index.html')
    else:
        return HttpResponse('usuario ou senha invalidos')


def index(request):
    return render(request, 'index.html')