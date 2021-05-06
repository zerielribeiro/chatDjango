from django.urls import re_path

from .consumers import ChatConsumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<nome_sala>\w+)/$', ChatConsumers),
]
