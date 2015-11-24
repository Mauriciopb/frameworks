"""Renderizar a una plantilla"""
from django.shortcuts import render, render_to_response
"""Regresar"""
from django.core.urlresolvers import reverse
"""Genera Paginacion"""
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import HttpResponseRedirect

#import time from calendar import month_name

from sistemaventas.models import Comentario

from django.forms import ModelForm
from django.core.context_processors import csrf

def poncomentario(request, pk):
	if request.method=='POST':
		formulario = ComentarioForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect(reverse("publicacion", args=[pk]))
	else:
		formulario = ComentarioForm()
	return render_to_response('publicacion.html', {'formulario':formulario}, context_instance=RequestContext(request))

	"""p = request.POST

	if 'mensaje' in p:
		autor = "Anonymous"

		if p["autor"]: autor = p["autor"]

		comentario = Comentario(identrada=Entrada.objects.get(pk=pk))
		cf = FormularioComentario(p,instance = comentario)
		cf.fields['autor'].required = False

		# commit = false para que no se auto guarde
		comentario = cf.save(commit = False)
		comentario.autor = autor
		# Graba el registro
		comentario.save()

	return HttpResponseRedirect(reverse("publicacion", args=[pk]))"""
