from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=125,blank=True, null=True)
    dt_nasc = models.DateField()
    email = models.CharField(max_length=125, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    pais = models.CharField(max_length=100, blank=True, null=True)
    senha = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return self.senha
    def __str__(self):
        return self.pais
    def __str__(self):
        return self.cidade
    def __str__(self):
        return self.email
    def __str__(self):
        return self.dt_nasc
    def __str__(self):
        return self.nome

class Mensagen(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=75, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    mensagem = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name
    def __str__(self):
        return self.mensagem
    def __str__(self):
        return self.email
    def __int__(self):
        return self.phone
