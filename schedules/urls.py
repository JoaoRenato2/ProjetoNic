from django.urls import path
from schedules.views import Register, Login, validar_cadastro, validar_login

urlpatterns = [
      # Home
    path('cadastro/', Register, name='cadastro'),
    path('login/', Login, name='login'),
    path('validar_cadastro/', validar_cadastro, name='validar_cadastro'),
    path('validar_login/', validar_login, name='validar_login'),
    
]