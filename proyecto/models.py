import datetime

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

class Usuario(models.Model):
	nomusu=models.CharField(max_length=200)
	data=models.DateTimeField("Fecha publicación usuario")
	def __str__(self):
		return self.nomusu

class Eleccion(models.Model):
	nombre=models.ForeignKey(Usuario, on_delete=models.CASCADE)
	texto=models.CharField(max_length=200)
	votos=models.IntegerField(default=0)
	def __str__(self):
                return self.pregunta

class EscojerUsuario(models.Model):
	usu=models.CharField(max_length=200)
	eleccion=models.CharField(max_length=200)
	voto=models.IntegerField(default=0)
	def __str__(self):
                return self.usu

# Create your models here.
