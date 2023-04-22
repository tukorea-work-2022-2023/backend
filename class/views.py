#from django.shortcuts import render

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
from rest_framework.filters import SearchFilter
from video_search import video_list_search

import requests
from io import BytesIO
from PIL import Image
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def video_search_list(request):
    VideoName = request.query_params.get('VideoName')
    video_list=video_list_search(VideoName)
    print(video_list)
    print(type(video_list))

    for i in range(10):
        if len(video_list[i])>0:

            title=video_list[i]['ten_title']
            link=book_result[i]['ten_link']
            view=book_result[i]['ten_view']
            created=book_result[i]['ten_created']

            print(title)
            return Response({'title': title,'link':link,'view':view,'created':created})

        else:
            return Response({'message': '동영상 리스트 조회에 오류가 있습니다.'})
