from hashlib import sha256
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse, request, JsonResponse
from django.shortcuts import redirect, render
import json
from validate_email import validate_email
from django.views import View
from schedules.models import Usuario


# Create your views here.
def home(request):
    return render(request, 'LandingPages.html')


def Login(request):
    return render(request, 'Login_Register.html')


def Register(request):
    
    return render(request, 'Login_Register.html')

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
                senha = sha256(senha.encode()).hexdigest()
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
    username = request.POST.get('username')
    senha = request.POST.get('senha')
    user_login = authenticate(username=username, senha=senha)
    if user_login:
        return render(request, 'index.html')
    else:
        return HttpResponse('usuario ou senha invalidos')


def index(request):
    return render(request, 'index.html')