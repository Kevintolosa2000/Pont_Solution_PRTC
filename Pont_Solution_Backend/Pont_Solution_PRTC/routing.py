from django.urls import re_path
from consumers.chat import ChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/chat_pont_solution/$', ChatConsumer.as_asgi()), # Ruta que estableci para las conexiones WebSocket
]
