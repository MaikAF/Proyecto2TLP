from rest_framework.serializers import ModelSerializer
from miapp.models import Evento

class EventoSerializer(ModelSerializer):
    class Meta:
        model = Evento
        fields = ['titulo', 'fecha_inicio', 'fecha_termino','tipo','segmento']