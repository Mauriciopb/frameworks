from django.shortcuts import render, render_to_response
from sistemaventas.models import Marca, Modelo
from sistemaventas.forms import MarcaForm
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

"""def lista_marcas(request):
	marcas = Marca.objects.all()
	return render_to_response("lista_marcas.html", {'marcas':marcas}, context_instance=RequestContext(request))"""

	
def lista_marcas(request):
	marcas = Marca.objects.all()
	return render_to_response("lista_marcas.html", dict(marcas = marcas), context_instance=RequestContext(request))

def lista_modelos(request, id_marca):
	dato = get_object_or_404 (Marca, pk=id_marca)
	return render_to_response("lista_modelos.html", {'modelo':dato}, context_instance=RequestContext(request))

def eliminar_marca(request,id_marca):
    instance = get_object_or_404(Marca, pk=id_marca)
    instance.delete()
    return HttpResponseRedirect('/marcas')