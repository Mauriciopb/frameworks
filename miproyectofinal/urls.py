"""miproyectofinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from sistemaventas.views import publicaciones

urlpatterns = [
    url(r'^publicaciones/', include('sistemaventas.urls', namespace='sistemaventas')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('social.apps.django_app.urls', namespace='social')),
    #url(r'^publicaciones/publicacion/(?P<id_publicacion>\d+)$', publicaciones.lista_publicaciones, name='lista_publicaciones'), 
    #url(r'^$', 'sistemaventas.views.inicio'), 
    #url(r'^$', include('sistemaventas.urls', namespace='sistemaventas')),
    #url(r'^publicacion/(?P<id_publicacion>\d+)$','sistemaventas.views.detalle_publicacion'), 
    #url(r'^publicacion/nuevo/$','sistemaventas.views.nueva_publicacion')

    #url(r'^marcas/$', 'sistemaventas.views.lista_marcas'), 

    #url(r'^publicaciones/$', 'sistemaventas.views.lista_publicaciones'),    
   #
    #url(r'^publicacion/nuevo/$','sistemaventas.views.nueva_publicacion')
 	#url(r'^$', include('home.urls')),
    #url(r'^home/', include('home.urls')),"""
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
