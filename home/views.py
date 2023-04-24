#from django.shortcuts import render
from .models import *
from .serializers import bookCommentSerializer,bookPostSerializer,bookPostCreateSerializer,bookCommentCreateSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view,permission_classes
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
import json
from rest_framework import filters
from django.views.generic import ListView
from django_filters.views import FilterView
from rest_framework.response import Response
from rest_framework import status

from django_filters.rest_framework import DjangoFilterBackend
from .permissions import CustomReadOnly
from rest_framework.filters import SearchFilter


import requests
from io import BytesIO
from PIL import Image
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

from book_search import barcode_book



# bookPost의 목록, detail 보여주기, 수정하기, 삭제하기 모두 가능

class bookPostViewSet(viewsets.ModelViewSet):


    queryset = bookPost.objects.all()
    authentication_classes = [BasicAuthentication,SessionAuthentication]
    permission_classes = [CustomReadOnly,IsAuthenticated]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'like']



    def get_serializer_class(self):
        if self.action == 'list' or 'retrieve':  # 전체 목록 또는 1개 조회

            return bookPostSerializer

        return bookPostCreateSerializer

    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)
        serializer.save(user=self.request.user, profile=profile)
        # tags_str을 파싱하여 tags_list로 변환
        # tags = self.request.data.get('tags')
        #
        # if tags is None:
        #     tags_list = []
        # else:
        #     try:
        #         tags_list = json.loads(tags)
        #     except ValueError:
        #         tags_list = []
        # serializer.save(user=self.request.user, profile=profile, tags_list=tags_list)
        # instance = serializer.instance
        # instance.tags.set(tags_list)









# 장바구니 기능
@api_view(['GET'])
@permission_classes([IsAuthenticated])  # 회원가입한 User라면 모두 진입 가능
def like_post(request, pk):
    """찜 기능: GET"""
    post = get_object_or_404(bookPost, pk=pk)

    if request.user == post.user:
        return Response({'status': status.HTTP_403_FORBIDDEN,
                         'message': '본인의 게시글은 찜을 할 수 없습니다.'})

    elif request.user in post.bucket.all():
        post.like.remove(request.user)
    else:
        post.like.add(request.user)
    return Response({'status': 'ok'})






# comment 보여주기, 수정하기, 삭제하기 모두 가능
class bookCommentViewSet(viewsets.ModelViewSet):
    """댓글 등록/조회/수정/삭제"""
    queryset = bookComment.objects.all()
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [CustomReadOnly,IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list' or 'retrieve':
            return bookCommentSerializer
        return bookCommentCreateSerializer

    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)
        serializer.save(user=self.request.user, profile=profile)



# 검색 기능
class bookSearchViewSet(viewsets.ModelViewSet):
    queryset=bookPost.objects.all()
    serializer_class = bookPostSerializer

    filter_backends = [SearchFilter]

    search_fields=['title']



# 바코드를 가지고 해당 서적 출력
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def barcode_book_info(request):
    ItemId = request.query_params.get('ItemId')
    book_result=barcode_book(ItemId)
    print(book_result)


    if "key" in book_result:
        title=book_result['title']
        author=book_result['author']
        publisher=book_result['publisher']
        #pubdate=book_result['pubdate']
        description=book_result['description']
        cover=book_result['cover']

        print(title)
        return Response({'title': title,'author':author,'publisher':publisher,'description':description,'cover':cover})

    else:
        return Response({'message': book_result})




