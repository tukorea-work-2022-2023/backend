#from django.shortcuts import render
from .models import *
from .serializers import bookCommentSerializer,bookPostSerializer,bookPostCreateSerializer,bookCommentCreateSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view,permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend
from .permissions import CustomReadOnly
from rest_framework.filters import SearchFilter




# bookPost의 목록, detail 보여주기, 수정하기, 삭제하기 모두 가능

class bookPostViewSet(viewsets.ModelViewSet):
    queryset = bookPost.objects.all()
    permission_classes = [CustomReadOnly]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'bucket']

    def get_serializer_class(self):
        if self.action == 'list' or 'retrieve':  # 전체 목록 또는 1개 조회
            return bookPostSerializer
        return bookPostCreateSerializer

    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)
        serializer.save(author=self.request.user, profile=profile)


# 장바구니 기능
@api_view(['GET'])
@permission_classes([IsAuthenticated])  # 회원가입한 User라면 모두 진입 가능
def bucket_post(request, pk):
    """찜 기능: GET"""
    post = get_object_or_404(bookPost, pk=pk)

    if request.user == post.author:
        return Response({'status': status.HTTP_403_FORBIDDEN,
                         'message': '본인의 게시글은 찜을 할 수 없습니다.'})

    elif request.user in post.bucket.all():
        post.bucket.remove(request.user)
    else:
        post.bucket.add(request.user)
    return Response({'status': 'ok'})






# comment 보여주기, 수정하기, 삭제하기 모두 가능
class bookCommentViewSet(viewsets.ModelViewSet):
    """댓글 등록/조회/수정/삭제"""
    queryset = bookComment.objects.all()
    permission_classes = [CustomReadOnly]

    def get_serializer_class(self):
        if self.action == 'list' or 'retrieve':
            return bookCommentSerializer
        return bookCommentCreateSerializer

    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)
        serializer.save(author=self.request.user, profile=profile)



# 검색 기능
class bookSearchViewSet(viewsets.ModelViewSet):
    queryset=bookPost.objects.all()
    serializer_class = bookPostSerializer

    filter_backends = [SearchFilter]

    search_fields=['title']

