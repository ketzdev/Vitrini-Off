from django.db import models
from django.contrib.auth.models import AbstractUser #importando a classe base do usuario
from django.db import models #estendendo a classe models
# Create your models here.

class Usuario(AbstractUser):
    TIPO_USUARIO_CHOICES = [
        ('CLIENTE', 'Cliente'), #primeiro é oq vai pro banco e o segundo é o que o usuario vai ver no forms
        ('ADMIN', 'Admin'),
    ]
    tipo_usuario = models.CharField('Tipo de Usuário',max_length=7, choices=TIPO_USUARIO_CHOICES, blank=False, null=False)
    
    def __str__(self):
        return self.username
    