from django.shortcuts import render

from django.shortcuts import render
from miapp.models import Evento
from api.serializers import EventoSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

@csrf_exempt
def ListaDeEventos(request):
 
    if request.method == 'GET':
        eventos = Evento.objects.all()
        serializer = EventoSerializer(eventos, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EventoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def ModificarEvento(request, pk):
    try:
        evento = Evento.objects.get(pk=pk)
    except Evento.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        evento = EventoSerializer(evento)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EventoSerializer(evento, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        evento.delete()
        return HttpResponse(status=204)

def home(request):
    return render(request, 'miapp/base.html', name='base')