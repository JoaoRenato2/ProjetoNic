from asyncio.windows_events import NULL
from hashlib import sha256
import re
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse, request, JsonResponse
from django.shortcuts import redirect, render
import json
from validate_email import validate_email
from django.views import View
from schedules.models import Usuario, Consultas
from django.contrib.auth.hashers import make_password



# Create your views here.
def home(request):
    
    return render(request, 'LandingPages.html')

def Login(request):
    status = request.GET.get('status')
    return render(request, 'Login_Register.html', {'status': status})

def Register(request):
    
    return render(request, 'Login_Register.html')

def index(request):
    return render(request, 'index.html')

def scheduling(request):
    return render(request, 'Scheduling.html')

def form(request):
    return render(request, 'Form.html')

def perfil(request):
    return render(request, 'perfil.html')

def perfilSenha(request):
    return render(request, 'perfil-senha.html')

def calendario(request):
    return render(request, 'calendar.html')

def sobre(request):
    return render(request, 'sobre.html')


def validar_cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        matricula = request.POST['username']
        email = request.POST['email']
        senha = request.POST['senha']

        if not Usuario.objects.filter(matricula=matricula).exists():
            if not Usuario.objects.filter(email=email).exists():
                if len(senha) < 8:
                    return HttpResponse("A senha deve ser maior que 8 caracteres")
                user = Usuario(nome=nome, matricula=matricula, email=email, senha=senha)
                user.senha = make_password(user.senha)
                user.save()
                success = 'Usuario Criado com sucesso'
                return HttpResponse(success)


class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_erro': 'A matricula deve conter apenas letra e numeros'}, status=400)
        if Usuario.objects.filter(nome=username).exists():
            return JsonResponse({'username_erro': 'Essa matricula já existe'}, status=400)
        return JsonResponse({'username_valid': True})


class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({'email_erro': 'Email invalido'}, status=400)
        if Usuario.objects.filter(email=email).exists():
            return JsonResponse({'email_erro': 'Esse email já existe'}, status=400)
        return JsonResponse({'email_valid': True})


def validar_login(request):
    matricula = request.POST['username']
    senha = request.POST['senha']
    User = authenticate(username=matricula, password=senha)
    if User is not None:

        login(request, User)
        return redirect('index/agendamento/')  
    else: 
        return redirect('/auth/login/?status=1')

def Appointment_Booking(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        categoria = request.POST.getlist('categoria')
        data = request.POST.get('data')
        hora = request.POST.get('hora')
        observacao = request.POST.get('observacao')
        if (nome != NULL):
            appointment = Consultas(name = nome, categoria = categoria, data = data, hora = hora, observacao = observacao)
            appointment.save()
            return redirect('/auth/index')
        
def sair(request):
    request.session.flush()
    return redirect('/auth/login')