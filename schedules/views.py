from asyncio.windows_events import NULL
from pipes import Template
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, request, JsonResponse
from django.shortcuts import redirect, render
from schedules.models import Usuario, Consultas
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.core.mail import EmailMessage
from django.conf import settings





# Create your views here.
def home(request):
    return render(request, 'LandingPages.html')

def Login(request):
    status = request.GET.get('status')
    return render(request, 'Login_Register.html', {'status': status})

def Register(request):
    return render(request, 'Login_Register.html')


def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    return redirect('/auth/login_erro/')


def scheduling(request):
    if request.user.is_authenticated:
        return render(request, 'Scheduling.html')
    return redirect('/auth/login_erro/')

def form(request):
    if request.user.is_authenticated:
        return render(request, 'Form.html')
    return redirect('/auth/login_erro/')
    


def perfil(request):
    if request.user.is_authenticated:
        return render(request, 'perfil.html')
    return redirect('/auth/login_erro/')
    


def perfilSenha(request):
    if request.user.is_authenticated:
        return render(request, 'perfil-senha.html')
    return redirect('/auth/login_erro/')
    


def calendario(request):
    if request.user.is_authenticated:
        return render(request, 'calendar.html')
    return redirect('/auth/login_erro/')

def sobre(request):
    return render(request, 'sobre.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def login_erro(request):
    return render(request, 'LoginRequest.html')



def validar_cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        matricula = request.POST['username']
        email = request.POST['email']
        senha = request.POST['senha']

        user = Usuario.objects.filter(username = matricula).first()

        if(user):
            return HttpResponse('Erro')
        user = Usuario.objects.create_user(username=nome, email = email, password = senha, matricula=matricula)
        user.save()
        return HttpResponse('suc')



        # if not Usuario.objects.filter(matricula=matricula).exists():
        #     if not Usuario.objects.filter(email=email).exists():
        #         if len(senha) < 8:
        #             return HttpResponse("A senha deve ser maior que 8 caracteres")
        #         user = User.objects.create_user(nome=nome, matricula=matricula, email=email, senha=senha)
        #         user.set_password(senha)
        #         user.save()
        #         success = 'Usuario Criado com sucesso'
        #         return HttpResponse(success)


# class UsernameValidationView(View):
#     def post(self, request):
#         data = json.loads(request.body)
#         username = data['username']
#         if not str(username).isalnum():
#             return JsonResponse({'username_erro': 'A matricula deve conter apenas letra e numeros'}, status=400)
#         if Usuario.objects.filter(nome=username).exists():
#             return JsonResponse({'username_erro': 'Essa matricula já existe'}, status=400)
#         return JsonResponse({'username_valid': True})


# class EmailValidationView(View):
#     def post(self, request):
#         data = json.loads(request.body)
#         email = data['email']
#         if not validate_email(email):
#             return JsonResponse({'email_erro': 'Email invalido'}, status=400)
#         if Usuario.objects.filter(email=email).exists():
#             return JsonResponse({'email_erro': 'Esse email já existe'}, status=400)
#         return JsonResponse({'email_valid': True})


def validar_login(request):
    matricula = request.POST['username']
    senha = request.POST['senha']
    user = authenticate(request ,matricula=matricula, password=senha)
    if user is not None:
        auth_login(request, user)
        return redirect('/auth/index/')  
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
        
def logout_view(request):
    logout(request)
    return redirect('/auth/login/')  

    # Redirect to a success page.

class SobreTemplateView(TemplateView):
    template_name: "sobre.html"

    def post(self,request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        email = EmailMessage(
            subject= f"{name} from Agendamento NIC",
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_HOST_USER],
            reply_to=[email]
        )
        email.send()
        return HttpResponse("suce")
