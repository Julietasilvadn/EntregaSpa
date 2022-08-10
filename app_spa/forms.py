from socket import fromshare
from django import forms

class PersonaFormulario(forms.Form):
    nombre=forms.CharField()
    apellido= forms.CharField()
    dni= forms.IntegerField()
    email= forms.EmailField()
    contraseña= forms.CharField()