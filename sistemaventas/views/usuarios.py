from django.shortcuts import render, render_to_response
from sistemaventas.models import Usuario
from sistemaventas.forms import UsuarioForm
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

def nuevo_usuario(request):
	formulario = UsuarioForm(request.POST, request.FILES)
	if request.method=='POST':		
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = UsuarioForm()
	return render_to_response('usuarioform.html', {'formulario':formulario}, context_instance=RequestContext(request))
