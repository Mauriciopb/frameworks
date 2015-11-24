from django import forms
from sistemaventas.models.publicacion import Publicacion
from django.utils.translation import ugettext_lazy as _

class PublicacionForm(forms.ModelForm):
	class Meta:
		model = Publicacion
		fields =['titulo', 'descripcion', 'precio', 'marca', 'modelo', 'usuario', 'ubicacion','imagen']
		widgets = {
			'titulo': forms.TextInput(attrs={'placeholder': 'Titulo','required':'true', 'class':'form-control', 'style':'width: 300px'}),
			'descripcion': forms.Textarea(attrs={'placeholder': 'Descripcion de la publicacion','required':'true', 'class':'form-control', 'style':'width: 300px'}),
			'precio': forms.TextInput(attrs={'placeholder': 'Precio','required':'true', 'class':'form-control', 'style':'width: 300px'}),
			'marca': forms.Select(attrs={'required':'true', 'class':'form-control', 'style':'width: 300px'}),
			'modelo': forms.Select(attrs={'required':'true', 'class':'form-control', 'style':'width: 300px'}),
			'usuario': forms.Select(attrs={'required':'true', 'class':'form-control', 'style':'width: 300px'}),
			'ubicacion': forms.TextInput(attrs={'placeholder': 'Ubicacion','required':'true', 'class':'form-control', 'style':'width: 300px'}),
			'fecha': forms.HiddenInput(),
			'imagen': forms.FileInput(attrs={'capture':"camera", 'accept':"image/*"}),
		}

		labels = {
			#'titulo': forms.
			'marca': _('Seleccione una marca'),
			'modelo':_('Seleccione un modelo'),
			'usuario': _('Seleccione un usuario'),
		}		
	