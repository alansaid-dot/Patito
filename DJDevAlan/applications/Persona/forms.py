from .models import Empleado
from django import forms


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
