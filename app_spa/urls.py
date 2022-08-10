from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('base/', mostrar_base, name= 'base'),
    path('persona-formulario', personaFormulario, name='form')
]