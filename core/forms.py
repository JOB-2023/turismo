# forms.py

from django import forms

class Formulariocontacto(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    correo = forms.EmailField(label='Correo electrónico', max_length=100)
    mensaje = forms.CharField(label='Mensaje', widget=forms.Textarea, max_length=250)
