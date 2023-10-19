from django.shortcuts import render
from AppOne.models import Curso
from django.http import HttpResponse

# Create your views here.

def crea_curso(self):
     curso = Curso(nombre='Python', camada=4545)
     curso.save()
     
     return HttpResponse(f'Se creo el curso de {curso.nombre} con el numero de camada {curso.camada}')