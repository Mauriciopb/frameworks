from django.shortcuts import render, render_to_response
from sistemaventas.models import Categoria

def listarCategorias(request):
    categorias = Categoria.objects.all()
    """template = loader.get_template('contactos/notas.html')
    form = NotaForm(request.POST or None)
    context = RequestContext(request, {
    'lista_notas': lista_notas,
    'form':form,
    'titulo_form':'Nota Nueva',
    'enviar_a':'registrar_nota',
    })
    return HttpResponse(template.render(context))"""
    return render_to_response("lista_categorias.html", {'categorias':categorias}, context_instance=RequestContext(request))

"""def registrarCategoria(request):
    form = NotaForm(request.POST or None)
    if form.is_valid():
        for key in form.cleaned_data:
            print ('llave---> ',key)
            print('valor->',form.cleaned_data.get(key))
        instance = form.save(commit = True)

    return HttpResponseRedirect(reverse('contactos:buscar_nota2', args=[instance.id,]))

def eliminar_nota(request,id_nota):
    instance = get_object_or_404(Nota, pk=id_nota)
    instance.delete()
    return HttpResponseRedirect(reverse('contactos:listar_notas_todas'))

def editar_nota(request , id_nota):

    form = NotaForm(request.POST or None)
    instancia = get_object_or_404(Nota, pk=id_nota)

    if form.is_valid():
        instancia = form.save(commit = False)
        instancia.id = id_nota    
        instancia.save()   

    print('persona' , request.POST['desde'])
    if request.POST['desde'] == 'notas':
        return HttpResponseRedirect(reverse('contactos:buscar_nota2', args=[instancia.id,]))
    return HttpResponseRedirect(reverse('contactos:buscar_nota', args=[instancia.id,]))