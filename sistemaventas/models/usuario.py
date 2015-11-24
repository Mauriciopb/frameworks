from django.db import models

class Usuario(models.Model):
	nombres = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=50)
	email = models.CharField(max_length=100)
	celular = models.CharField(max_length=20)
	#contra = models.CharField()
	def __str__(self):
		return self.nombres