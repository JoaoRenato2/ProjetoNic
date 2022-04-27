from django.urls import path

from schedules.views import home, Login_Register

urlpatterns = [
    path('', home),  # Home
    path('Login_Register.html', Login_Register),
]