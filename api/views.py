from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from miapp.models import Evento
from api.serializers import EventoSerializer

class EventoApiViewSet(ModelViewSet):
    serializer_class= EventoSerializer
    queryset = Evento.objects.all()