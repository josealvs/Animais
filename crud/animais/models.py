from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class EmailUsuario (models.Model):
 
    idemail = models.AutoField(primary_key = True)
 
    email = models.CharField(max_length = 20)

class Usuario (models.Model):
    
    idUsuario = models.AutoField(primary_key = True)

    username = models.CharField(max_length = 20)

    nome = models.CharField(max_length=100)
    
    senha = models.CharField(max_length = 8)

    id_usu_email = models.ForeignKey(EmailUsuario, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.nome

class EmailAdministrador (models.Model):
 
    idemail = models.AutoField(primary_key = True)
 
    email = models.CharField(max_length = 20)
 

class Administrador (models.Model):
    
    idAdministrador = models.AutoField(primary_key = True)

    username = models.CharField(max_length = 20)

    nome = models.CharField(max_length=100)
    
    senha = models.CharField(max_length = 8)

    id_ema_adm = models.ForeignKey(EmailAdministrador, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.nome


class Cidade(models.Model):
    codCidade = models.AutoField(primary_key = True)

    nome = models.CharField(max_length = 20)

    def __str__(self):
        return self.nome

class Situacao(models.Model):
    codSituacao = models.AutoField(primary_key = True)

    situacao = models.CharField(max_length = 20)

    def __str__(self):
        return self.situacao

class Estado(models.Model):
    codEstado = models.AutoField(primary_key = True)

    estado = models.CharField(max_length = 20)

    def __str__(self):
        return self.estado

class Denuncia (models.Model):

    codDenuncia = models.AutoField(primary_key = True)

    animal = models.CharField(max_length = 20)
    
    descricao = models.CharField(max_length = 200)
    
    data = models.DateField()
    
    local = models.CharField(max_length = 100)

    usuario = models.ForeignKey(User, on_delete = models.PROTECT, default = None, null = True)

    cidade = models.ForeignKey(Cidade, on_delete = models.CASCADE, default = None, null = True)

    situacao = models.ForeignKey(Situacao, on_delete = models.CASCADE, default = None, null = True)
    

class Resgate(models.Model):
    codResgate = models.AutoField(primary_key = True)

    animal = models.CharField(max_length = 20)
    
    descricao = models.CharField(max_length = 200)
    
    data = models.DateField()
    
    local = models.CharField(max_length = 100)

    usuario = models.ForeignKey(User, on_delete = models.PROTECT, default = None, null = True)

    cidade = models.ForeignKey(Cidade, on_delete = models.CASCADE, default = None, null = True)

    situacao = models.ForeignKey(Situacao, on_delete = models.CASCADE, default = None, null = True)

    estado = models.ForeignKey(Estado, on_delete = models.CASCADE, default = None, null = True)
