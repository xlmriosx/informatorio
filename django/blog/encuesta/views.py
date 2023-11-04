from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Pregunta

def index(request):
    preguntas = Pregunta.objects.get(pregunta='Cuantos continentes existen?')
    return HttpResponse(f"{preguntas.id}")

    