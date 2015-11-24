from django.db import models
from sistemaventas.models.categoria import Categoria

class Marca(models.Model):
	nombre = models.CharField(max_length=10)
	categoria = models.ForeignKey(Categoria)
	def __str__(self):
		return self.nombre