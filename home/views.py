#from django.shortcuts import render
from .models import *
from .serializers import bookCommentSerializer, bookPostSerializer, bookPostCreateSerializer, StudySerializer
from .serializers import bookCommentSerializer,bookPostSerializer,bookPostCreateSerializer,bookCommentCreateSerializer
from rest_framework import viewsets, generics
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
import json
from rest_framework import filters
from django.views.generic import ListView
from django_filters.views import FilterView
from rest_framework.views import APIView
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
import datetime
from django.utils import timezone
from datetime import timedelta

from book_search import barcode_book



# bookPost의 목록, detail 보여주기, 수정하기, 삭제하기 모두 가능

class bookPostViewSet(viewsets.ModelViewSet):


    queryset = bookPost.objects.all()
    authentication_classes = [JWTAuthentication]
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


    # 조회수 기능
    def retrieve(self, request, pk=None):

        instance = get_object_or_404(self.get_queryset(), pk=pk)
        # 당일날 밤 12시에 쿠키 초기화
        tomorrow = datetime.datetime.replace(timezone.datetime.now(), hour=23, minute=59, second=0)
        expires = datetime.datetime.strftime(tomorrow, "%a, %d-%b-%Y %H:%M:%S GMT")

        # response를 미리 받고 쿠키를 만들어야 한다
        serializer = self.get_serializer(instance)
        response = Response(serializer.data, status=status.HTTP_200_OK)
        # 쿠키 읽기 & 생성
        if request.COOKIES.get('hit') is not None:  # 쿠키에 hit 값이 이미 있을 경우
            cookies = request.COOKIES.get('hit')
            cookies_list = cookies.split('|')  # '|'는 다르게 설정 가능 ex) '.'
            if str(pk) not in cookies_list:
                response.set_cookie('hit', cookies + f'|{pk}', expires=expires)  # 쿠키 생성
                instance.hits += 1
                instance.save()

        else:  # 쿠키에 hit 값이 없을 경우(즉 현재 보는 게시글이 첫 게시글임)
            response.set_cookie('hit', pk, expires=expires)
            instance.hits += 1
            instance.save()

        # hits가 추가되면 해당 instance를 serializer에 표시
        serializer = self.get_serializer(instance)

        return response


class BookListByTag(APIView):
    def get(self, request, tag_name):
        books =bookPost.objects.filter(tags__name__in=[tag_name])
        serializer = bookPostSerializer(books, many=True)
        return Response(serializer.data)

# 장바구니 기능
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])  # 회원가입한 User라면 모두 진입 가능
def like_post(request, pk):
    """찜 기능: GET"""
    post = get_object_or_404(bookPost, pk=pk)


    if request.user == post.user:
        return Response({'status': status.HTTP_403_FORBIDDEN,
                         'message': '본인의 게시글은 찜을 할 수 없습니다.'})

    elif request.user in post.like.all():
        post.like.remove(request.user)
    else:
        post.like.add(request.user)
    return Response({'status': 'ok'})


# comment 보여주기, 수정하기, 삭제하기 모두 가능
class bookCommentViewSet(viewsets.ModelViewSet):
    """댓글 등록/조회/수정/삭제"""
    queryset = bookComment.objects.all()
    authentication_classes = [JWTAuthentication]
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
@authentication_classes([JWTAuthentication])
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

# - 스터디 -
class StudyViewSet(viewsets.ModelViewSet):
    queryset = Study.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'book_post']

    def get_serializer_class(self):
        return StudySerializer

    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)
        serializer.save(user=self.request.user,profile=profile)

class StudyListByBookPost(generics.ListAPIView):
    serializer_class = StudySerializer

    def get_queryset(self):
        book_post_id = self.kwargs['book_post_id']
        return Study.objects.filter(book_post_id=book_post_id)


# - 마이페이지 -
# 내가 등록한 게시물
class MyPageView(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        user = request.user.id
        posts = bookPost.objects.filter(user_id=user).order_by("-id")
        serialized_data = bookPostSerializer(posts, many=True).data

        return Response(serialized_data, status=status.HTTP_200_OK)



# 내가 찜한 게시물
# class MyLikeView(APIView):
#     authentication_classes = [JWTAuthentication]
#
#     def get(self, request):
#         user = request.user.id
#         likes = like_post.objects.filter(user_id=user).order_by("-id")
#
#         serialized_data = bookPostSerializer(likes, many=True).data
#
#         return Response(serialized_data, status=status.HTTP_200_OK)


# 대여 일자에 따른 대여 일수
@api_view(["POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create_rental(request,pk):
    book = bookPost.objects.get(pk=pk)
    rental_days = request.data.get('rental_days')
    start_date = timezone.now().date()
    print(start_date)
    end_date = start_date + timedelta(days=rental_days)
    print(end_date)
    book.rent_state="대여중"
    book.rent_start_date = start_date
    book.rent_end_date = end_date

    book.save()

    return Response({'message': 'Rental created successfully.'})