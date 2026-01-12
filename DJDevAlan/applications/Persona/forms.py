from .models import Empleado
from django import forms
from .models import Habilidades


class EmpleadoForm(forms.ModelForm):

    class Meta:
        model = Empleado
        fields = (
            'first_name',
            'last_name',
            'job',
            'departamento',
            'avatar',
            'Habilidades',
        )
        widgets = {
            'Habilidades': forms.CheckboxSelectMultiple()
        }
        
class HabilidadForm(forms.ModelForm):
    """Formulario para crear nuevas habilidades"""
    
    class Meta:
        model = Habilidades
        fields = ('habilidad',)
        widgets = {
            'habilidad': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese la habilidad',
                    'class': 'form-control'
                }
            )
        }
    
    def clean_habilidad(self):
        habilidad = self.cleaned_data['habilidad']
        # Validar que no exista una habilidad con el mismo nombre
        if Habilidades.objects.filter(habilidad__iexact=habilidad).exists():
            raise forms.ValidationError('Esta habilidad ya existe')
        return habilidad
