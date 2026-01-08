from django import forms

class NewDepartamentoForm(forms.Form):
    departamento = forms.CharField(max_length=50)
    short_name = forms.CharField(max_length=50)
