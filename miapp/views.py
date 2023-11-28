from django.shortcuts import render
from django.http import HttpResponse
from .models import Evento

from django.shortcuts import render
from miapp.models import Evento
from api.serializers import EventoSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User, Group

def home(request):
    
    eventos = Evento.objects.all()

    data = {
        'title': 'Inicio',
        'evento': eventos,
    }

    return render(request, 'miapp/tabla.html', data)

