from django.urls import re_path, path
#from .consumers import ChatConsumer
from . import consumers
# websocket_patterns = [
#     path('chat/<str:user_id>/', ChatConsumer.as_asgi())
# ]

websocket_urlpatterns = [
    path('chat/<str:room_name>', consumers.ChatConsumer.as_asgi()),
]