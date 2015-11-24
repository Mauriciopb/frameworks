from django.db import models
from django.utils import timezone
from datetime import datetime 
from sistemaventas.models.marca import Marca
from sistemaventas.models.modelo import Modelo
from sistemaventas.models.usuario import Usuario
from uuid import uuid4
import os


class Publicacion(models.Model):

	titulo = models.CharField(max_length=20)
	descripcion = models.TextField()
	precio = models.IntegerField(default = 0 , null = True , blank = True)
	marca = models.ForeignKey(Marca)
	modelo = models.ForeignKey(Modelo)
	usuario = models.ForeignKey(Usuario)
	ubicacion = models.CharField(max_length=30)
	fecha_pu = models.DateTimeField(default=datetime.now )
	imagen = models.ImageField(upload_to='publicaciones')	

	def __str__(self):
		return self.titulo

