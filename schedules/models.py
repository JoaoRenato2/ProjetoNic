from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    matricula = models.CharField(max_length=50, null=True)
    email = models.EmailField()
    senha = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.matricula

class Consultas(models.Model):
    name = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50, null=True)
    data = models.CharField(max_length=50)
    hora = models.CharField(max_length=50)
    observacao = models.TextField(blank=True)
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.data




