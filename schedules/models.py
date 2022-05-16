from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    matricula = models.CharField(max_length=50, null=True)
    email = models.EmailField()
    senha = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.matricula

