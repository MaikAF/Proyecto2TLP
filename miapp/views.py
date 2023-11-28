from django.shortcuts import render
from django.http import HttpResponse
from .models import Evento

def home(request):

    evento = Evento.objects.all()

    data = {
        'title': 'Inicio',
        'evento': evento,
    }

    return render(request, 'miapp/base.html', data)