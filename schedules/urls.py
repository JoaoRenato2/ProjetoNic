import django
from django.urls import path
from schedules.views import Register, Login, form, scheduling, validar_cadastro, validar_login, index, UsernameValidationView, EmailValidationView, Appointment_Booking
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
      # Home
    path('cadastro/', Register, name='cadastro'),
    path('login/', Login, name='login'),
    path('validar_cadastro/', validar_cadastro, name='validar_cadastro'),
    path('validar_login/', validar_login, name='validar_login'),
    path('index/', index, name='index'),
    path('index/agendamento/', scheduling, name='agendamento'),
    path('index/agendamento/form/', form, name='form'),
    path('validate-username', csrf_exempt(UsernameValidationView.as_view()), name='validate-username'),
    path('validate-email', csrf_exempt(EmailValidationView.as_view()), name='validate-email'),
    path('booking', Appointment_Booking, name='booking'),

    
]