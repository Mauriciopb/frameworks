from django.contrib import admin
from sistemaventas.models import Marca, Modelo, Usuario, Publicacion, Categoria, Comentario

# Register your models here.
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Usuario)
admin.site.register(Publicacion)
admin.site.register(Categoria)
admin.site.register(Comentario)
