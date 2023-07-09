from django.db import models

from account.models import UserData
from home.models import bookPost


class ChatParticipantsChannel(models.Model):
    channel = models.CharField(max_length=256)
    user = models.ForeignKey(UserData, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.channel)


class ChatRoom(models.Model):
    name = models.CharField(max_length=256)
    last_message = models.CharField(max_length=1024, null=True)
    last_sent_user = models.ForeignKey(
        UserData, on_delete=models.PROTECT, null=True)
    post=models.ForeignKey(bookPost, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Messages(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.PROTECT)
    user = models.ForeignKey(UserData, on_delete=models.PROTECT)
    content = models.CharField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


class ChatRoomParticipants(models.Model):
    user = models.ForeignKey(UserData, on_delete=models.PROTECT)
    room = models.ForeignKey(ChatRoom, on_delete=models.PROTECT)