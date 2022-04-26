from django.urls import path

from schedules.views import home

urlpatterns = [
    path('', home)  # Home
]