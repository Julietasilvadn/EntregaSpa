from django.shortcuts import render
from app_spa.forms import *
from .models import *

def mostrar_base(request):
    return render(request, "app_spa/base.html")

def personaFormulario(request):
    if request.method == "POST":
        miFormulario = PersonaFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            persona = Persona(nombre= informacion['nombre'], apellido= informacion['apellido'], dni= informacion['dni'], email= informacion['email'], contraseña= informacion['contraseña'])
            persona.save()
            return render(request, "app_spa/base.html")
    else:
        miFormulario= PersonaFormulario()
    return render(request, "app_spa/persona_form.html", {"miFormulario":miFormulario})