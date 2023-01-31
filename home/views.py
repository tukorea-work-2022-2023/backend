#from django.shortcuts import render
from .models import *
from .serializers import bookCommentSerializer,bookPostSerializer
from rest_framework import viewsets

# 토큰 형식으로 바꿔줘야 함.
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly




# bookPost의 목록, detail 보여주기, 수정하기, 삭제하기 모두 가능

class bookPostViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication,SessionAuthentication]
    permission_classes = [IsOwnerOrReadOnly,IsAuthenticatedOrReadOnly]

    queryset = bookPost.objects.all()
    serializer_class = bookPostSerializer

    def perform_create(self, serializer):
        bookPost.update_counter
        # 왜?
        serializer.save(user=self.request.user)


# comment 보여주기, 수정하기, 삭제하기 모두 가능
class bookCommentViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication,SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    queryset = bookComment.objects.all()
    serializer_class = bookCommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class bookSearchViewSet(viewsets.ViewSet):

    def list(self,request):
        queryset=bookSearch.objects.all()
        serializer=bookSearchViewSet(queryset,many=True)
        return Response(serializer.data)
