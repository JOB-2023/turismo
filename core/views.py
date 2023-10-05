   
    # finegap/views.py

from django.shortcuts import render, redirect
from .forms import Formulariocontacto
from .models import Persona
from .models import FormContacto
from django.urls import reverse

def home(request):
    return render(request, 'core/home.html')

# def contacto(request):
#     return render(request, 'core/contacto.html')


def contacto(request):
    if request.method == 'POST':
        form = Formulariocontacto(request.POST)
        if form.is_valid():
            # Procesar el formulario si es válido
            nombre = form.cleaned_data['nombre']
            correo = form.cleaned_data['correo']
            mensaje = form.cleaned_data['mensaje']
            # Puedes realizar acciones adicionales aquí, como enviar un correo electrónico o guardar en la base de datos
            contacto = FormContacto(nombre=nombre,correo=correo,mensaje=mensaje)
            contacto.save()
            return redirect(reverse("home"))
    else:
        # Mostrar un formulario en blanco si no se ha enviado
        form = Formulariocontacto()

    return render(request, 'core/contacto.html', {'form': form})


def acerca_de(request):
    return render(request, 'core/acerca_de.html')

def destinos(request, destino):
     return render(request, "core/destinos.html", {
        "destino": destino
    })