from django.shortcuts import render, render_to_response
from sistemaventas.models import Publicacion
from django.template import RequestContext
from sistemaventas.forms import PublicacionForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib.auth import logout
from django.core.mail import send_mail , BadHeaderError
from django.conf import settings
from django.core.urlresolvers import reverse
from datetime import date
import os 

def inicio(request):
	publicaciones = Publicacion.objects.all()
	return render_to_response('inicio.html', dict(publicaciones = publicaciones), context_instance=RequestContext(request))

def nueva_publicacion(request):
	formulario = PublicacionForm(request.POST, request.FILES)
	if request.method=='POST':		
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = PublicacionForm()
	return render_to_response('publicacionform.html', {'formulario':formulario}, context_instance=RequestContext(request))

def detalle_publicacion(request, id_publicacion):
	dato = get_object_or_404 (Publicacion, pk=id_publicacion)
	#comentarios = Comentario.objects.filter(Publicacion=dato)
	return render_to_response("publicacion.html", {'publicacion':dato}, context_instance=RequestContext(request))

def lista_publicaciones(request):
	publicaciones = Publicacion.objects.all()
	return render_to_response("lista_publicaciones.html", {'publicaciones':publicaciones}, context_instance=RequestContext(request))

def editar_publicacion(request, id_publicacion):

    form = PublicacionForm(request.POST or None)
    instancia = get_object_or_404(Publicacion, pk=id_publicacion)

    if form.is_valid():
        instancia = form.save(commit = False)
        instancia.id = idpublicacion    
        instancia.save()   

    #if request.POST['desde'] == 'notas':
        #return HttpResponseRedirect(reverse('contactos:buscar_nota2', args=[instancia.id,]))
    return HttpResponseRedirect('/publicaciones')

def eliminar_publicacion(request,id_publicacion):
    instance = get_object_or_404(Publicacion, pk=id_publicacion)
    instance.delete()
    return HttpResponseRedirect('/publicaciones')