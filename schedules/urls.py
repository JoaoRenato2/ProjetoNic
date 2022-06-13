import django
from django.urls import path
from schedules.views import Register, Login, form, scheduling, validar_cadastro, validar_login, index, Appointment_Booking, perfil, perfilSenha, calendario, sobre, cadastro,logout_view, SobreTemplateView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
      # Home
    path('cadastro/', cadastro, name='cadastro'),
    path('login/', Login, name='login'),
    path('validar_cadastro/', validar_cadastro, name='validar_cadastro'),
    path('validar_login/', validar_login, name='validar_login'),
    path('index/', index, name='index'),
    path('index/agendamento/', scheduling, name='agendamento'),
    path('index/agendamento/form/', form, name='form'),
    # path('validate-username', csrf_exempt(UsernameValidationView.as_view()), name='validate-username'),
    # path('validate-email', csrf_exempt(EmailValidationView.as_view()), name='validate-email'),
    path('booking', Appointment_Booking, name='booking'),
    path('index/perfil/', perfil, name='perfil'),
    path('index/perfil/senha/', perfilSenha, name='perfil-senha'),
    path('index/calendario/', calendario, name='calendario'),
    path('index/sobre/', sobre, name='sobre'),
    path('index/logout/', logout_view, name='logout'),
    path('index/sobre/email/', SobreTemplateView.as_view(), name='sobre_email'),

    


    
]