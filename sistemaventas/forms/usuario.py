from django import forms
from sistemaventas.models.usuario import Usuario

class UsuarioForm(forms.ModelForm):
	class Meta:
		model = Usuario
		fields =['nombres', 'apellidos', 'email', 'celular']
		widgets = {
			'nombres': forms.TextInput(attrs={'placeholder': 'Nombres', 'required':'true' , 'class':'form-control', 'style':'width: 300px'}),
			'apellidos': forms.TextInput(attrs={'placeholder': 'Apellidos', 'required':'true' , 'class':'form-control', 'style':'width: 300px'}),
			'email': forms.TextInput(attrs={'placeholder': 'Email', 'required':'true' , 'class':'form-control', 'style':'width: 300px'}),
			'celular': forms.TextInput(attrs={'placeholder': 'Celular', 'required':'true' , 'class':'form-control', 'style':'width: 300px'}),
		}
