from django.shortcuts import render
from django.http import HttpResponse
from json import loads,dumps
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from . serializers import EstudianteSerializer, IntentosSerializer, JuegoSerializer
from . models import Estudiante, Intentos, Juego
from random import randrange
import sqlite3
import requests, json

def index(request):
    return render(request, 'index.html')

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

class IntentosViewSet(viewsets.ModelViewSet):
    queryset = Intentos.objects.all()
    serializer_class = IntentosSerializer

class JuegoViewSet(viewsets.ModelViewSet):
    queryset = Juego.objects.all()
    serializer_class = JuegoSerializer

def charts(request):
    data = [["Numero de lista", "Progreso"]]
    url = "http://20.127.156.252:8002/apiestudiante"
    header={
        "Content-Type":"application/json"
    }
    
    result = requests.get(url, headers=header)
    result_new= result.json()
    for i in range(len(result_new)): 
        if result_new[i]['grupo'] == "A":
            data.append([result_new[i]['num_lista'], result_new[i]['progreso']])
    
    modified_data = dumps(data)
    return render(request,'charts.html',{'values':modified_data,})