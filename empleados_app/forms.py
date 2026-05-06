from django import forms
from .models import Departamento, Empleado


class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombre', 'ubicacion', 'descripcion', 'foto']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-input'}),
            'ubicacion': forms.TextInput(attrs={'class': 'form-input'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-input', 'rows': 3}),
        }


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombres', 'apellidos', 'cargo', 'foto', 'departamento']
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-input'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-input'}),
            'cargo': forms.TextInput(attrs={'class': 'form-input'}),
            'departamento': forms.Select(attrs={'class': 'form-input'}),
        }
