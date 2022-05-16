import django
from django.urls import path
from schedules.views import Register, Login, validar_cadastro, validar_login, index, UsernameValidationView, EmailValidationView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
      # Home
    path('cadastro/', Register, name='cadastro'),
    path('login/', Login, name='login'),
    path('validar_cadastro/', validar_cadastro, name='validar_cadastro'),
    path('validar_login/', validar_login, name='validar_login'),
    path('index/', index, name='index'),
    path('validate-username', csrf_exempt(UsernameValidationView.as_view()), name='validate-username'),
    path('validate-email', csrf_exempt(EmailValidationView.as_view()), name='validate-email'),

    
]