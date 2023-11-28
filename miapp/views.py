from django.shortcuts import render
from django.http import HttpResponse
from .models import Evento

from django.shortcuts import render
from miapp.models import Evento
from api.serializers import EventoSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


def home(request):

    evento = Evento.objects.all()

    data = {
        'title': 'Inicio',
        'evento': evento,
    }

    return render(request, 'miapp/base.html', data)