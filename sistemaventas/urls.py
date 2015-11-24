from django.conf.urls import url
from .views import publicaciones, marcas, usuarios, comentario
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	# INICIO
	url(r'^admin$', include(admin.site.urls)),
    url(r'^$', publicaciones.inicio, name='inicio'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    #url(r'^$', IndexView.as_view()),
    url(r'^publicacion/(?P<id_publicacion>[0-9]+)$', publicaciones.detalle_publicacion, name='detalle_publicacion'), 
	url(r'^publicaciones$', publicaciones.lista_publicaciones, name = 'lista_publicaciones'),
    url(r'^publicacion/nuevo', publicaciones.nueva_publicacion, name='nueva_publicacion'),
    url(r'^publicaciones/editar/(?P<id_publicacion>[0-9]+)$',publicaciones.editar_publicacion,name = 'editar_publicacion'),
    url(r'^publicaciones/eliminar/(?P<id_publicacion>[0-9]+)$',publicaciones.eliminar_publicacion,name = 'eliminar_publicacion'),
    

    # MARCAS
    url(r'^marcas$', marcas.lista_marcas, name='lista_marcas'),   
    url(r'^marca/(?P<id_marca>[0-9]+)$', marcas.lista_modelos, name='lista_modelos'), 
    url(r'^marca/eliminar/(?P<id_marca>[0-9]+)$',marcas.eliminar_marca,name = 'eliminar_marca'),

    # USUARIOS
	url(r'^usuario/nuevo', usuarios.nuevo_usuario, name='nuevo_usuario'),   
	#url(r'^comentario/nuevo', comentario.poncomentario, name='poncomentario'),   
	

    """url(r'^salir/$', contactos.salir ,name = 'salir'),
    url(r'^opciones/$', contactos.opciones, name='opciones'),
    url(r'^actualizar_aspecto/$', contactos.actualizar_aspecto, name='actualizar_aspecto'),
    url(r'^enviar_contactos_email/$', contactos.enviar_contactos_email, name='enviar_contactos_email'),
    url(r'^enviar_contactos_archivo/$', contactos.enviar_contactos_archivo, name='enviar_contactos_archivo'),"""
    
    # MARCAS

    # CONTACTENOS

]