from django.contrib import admin
from .models import ChatRoom, Messages, ChatParticipantsChannel, ChatRoomParticipants

# 관리자 페이지에서 관리
admin.site.register(ChatRoomParticipants)
admin.site.register(ChatRoom)
admin.site.register(Messages)
admin.site.register(ChatParticipantsChannel)