from django.db import models
from sistemaventas.models.usuario import Usuario

class Contacto(models.Model):
    usuario = models.ForeignKey(Usuario)
    descripcion = models.CharField(max_length = 50)

    def __str__(self):
        return self.descripcion

    class Meta:
        app_label = 'contactos'

