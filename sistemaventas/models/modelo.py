from django.db import models
from sistemaventas.models.marca import Marca

class Modelo(models.Model):
	nombre = models.CharField(max_length=10)
	marca = models.ForeignKey(Marca)
	def __str__(self):
		return self.nombre