from django import forms
from .models import Prueba

class PruebaForm(forms.ModelForm):
    
    class Meta:
        model = Prueba
        fields = ('titulo', 'subtitulo', 'cantidad')
    
        widgets = {
            'titulo': forms.TextInput(attrs={
                'placeholder': 'Ingrese texto aquí'
            }),
        }

    
    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        if cantidad<10:
            raise forms.forms.ValidationError('Ingrese un numero mayor a 10')
         # TODO Validation
        return cantidad