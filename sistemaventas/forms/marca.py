from django import forms
from sistemaventas.models.marca import Marca

class MarcaForm(forms.ModelForm):
	class Meta:
		model = Marca
		fields =['nombre', 'categoria']
		widgets = {
			'nombre': forms.TextInput(attrs={'placeholder': 'Nombre', 'required':'true' , 'class':'form-control', 'style':'width: 300px'}),
			'categoria': forms.TextInput(attrs={'required':'true' , 'class':'form-control', 'style':'width: 300px'}),
		}
