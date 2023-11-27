from rest_framework.routers import DefaultRouter
from api.views import EventoApiViewSet

router_evento = DefaultRouter()
router_evento.register(prefix='miapp', basename='miapp', viewset= EventoApiViewSet)