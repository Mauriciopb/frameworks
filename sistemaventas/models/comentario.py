from django.db import models
from sistemaventas.models.publicacion import Publicacion


class Comentario(models.Model):
	fechacomentario = models.DateTimeField(auto_now_add=True)
	autor = models.CharField(max_length=100)
	mensaje = models.TextField()
	idpublicacion = models.ForeignKey(Publicacion)

	def __str__(self):
		return str("%s %s" %(self.idpublicacion, self.mensaje[:60]))