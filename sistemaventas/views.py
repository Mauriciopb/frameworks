from django.shortcuts import render, render_to_response
from sistemaventas.models import Publicacion,Marca
from django.template import RequestContext
from sistemaventas.forms import PublicacionForm, MarcaForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404

# Create your views here.
def inicio(request):
	publicaciones = Publicacion.objects.all()
	return render_to_response('inicio.html', dict(publicaciones = publicaciones), context_instance=RequestContext(request))

def lista_marcas(request):
	marcas = Marca.objects.all()
	return render_to_response("lista_marcas.html", {'marcas':marcas}, context_instance=RequestContext(request))

def nueva_publicacion(request):
	formulario = PublicacionForm(request.POST, request.FILES)
	if request.method=='POST':		
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/publicaciones')
	else:
		formulario = PublicacionForm()
	return render_to_response('publicacionform.html', {'formulario':formulario}, context_instance=RequestContext(request))

def lista_publicaciones(request):
	publicaciones = Publicacion.objects.all()
	return render_to_response("lista_publicaciones.html", {'publicaciones':publicaciones}, context_instance=RequestContext(request))

def detalle_publicacion(request, id_publicacion):
	dato = get_object_or_404 (Publicacion, pk=id_publicacion)
	#comentarios = Comentario.objects.filter(Publicacion=dato)
	return render_to_response("publicacion.html", {'publicacion':dato}, context_instance=RequestContext(request))

