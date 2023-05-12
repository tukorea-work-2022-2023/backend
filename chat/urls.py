from django.urls import path
from .views import *

urlpatterns = [
    path('chat/room-messages/<str:user_id>/', RoomMessagesView.as_view(), name='room_messages'),
    path('chat/room-messages/<str:user_id>/<int:room_id>/', RoomMessagesView.as_view(), name='room_messages'),

    path('chat/user-chatrooms/', ChatRoomListView.as_view(), name='user_chatrooms')
]