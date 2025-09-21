from django.db import models

# Create your models here.


class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Servico(models.Model):
    nome_cliente = models.CharField(max_length=100)
    data_servico = models.DateField()
    tipo_servico = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome_cliente} - {self.tipo_servico}"