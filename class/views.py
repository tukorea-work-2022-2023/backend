#from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
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
import pymysql




# database 연결
conn = pymysql.connect(host='127.0.0.1', user='root', password='dahee1228!', db='crawling_video', charset='utf8')
cursor = conn.cursor()


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def video_search_list(request):
    VideoName = request.query_params.get('VideoName')
    data=[]
    if 'C언어'==VideoName:
        cursor.execute("SELECT * FROM crawling_video.CLanguage_videos")
        data = cursor.fetchall()
    elif '파이썬'==VideoName:
        cursor.execute("SELECT * FROM crawling_video.python_videos")
        data = cursor.fetchall()
    elif '자바'==VideoName:
        cursor.execute("SELECT * FROM crawling_video.java_videos")
        data = cursor.fetchall()
    elif 'SQL'==VideoName:
        cursor.execute("SELECT * FROM crawling_video.sql_videos")
        data = cursor.fetchall()
    elif 'HTML+CSS+자바스크립트'==VideoName:
        cursor.execute("SELECT * FROM crawling_video.html_videos")
        data = cursor.fetchall()
    elif '코틀린'==VideoName:
        cursor.execute("SELECT * FROM crawling_video.cotlin_videos")
        data = cursor.fetchall()
    elif 'IT 트렌드'==VideoName:
        cursor.execute("SELECT * FROM crawling_video.it_trend_videos")
        data = cursor.fetchall()
    elif '개발자 면접'==VideoName:
        cursor.execute("SELECT * FROM crawling_video.interview_videos")
        data = cursor.fetchall()
    elif '백엔드'==VideoName:
        cursor.execute("SELECT * FROM crawling_video.backend_videos")
        data = cursor.fetchall()
    elif '프론트엔드'==VideoName:
        cursor.execute("SELECT * FROM crawling_video.frontend_videos")
        data = cursor.fetchall()
    elif '앱개발'==VideoName:
        cursor.execute("SELECT * FROM crawling_video.app_videos")
        data = cursor.fetchall()
    elif '정보보안'==VideoName:
        cursor.execute("SELECT * FROM crawling_video.security_videos")
        data = cursor.fetchall()
    elif 'Spring Boot'==VideoName:
        cursor.execute("SELECT * FROM crawling_video.springboot_videos")
        data = cursor.fetchall()
    elif '스프링 프레임워크'==VideoName:
        cursor.execute("SELECT * FROM crawling_video.springframework_videos")
        data = cursor.fetchall()
    elif 'Python Django'==VideoName:
        cursor.execute("SELECT * FROM crawling_video.django_videos")
        data = cursor.fetchall()
    elif 'Python Flask'==VideoName:
        cursor.execute("SELECT * FROM crawling_video.flask_videos")
        data = cursor.fetchall()
    elif 'Node.js'==VideoName:
        cursor.execute("SELECT * FROM crawling_video.nodejs_videos")
        data = cursor.fetchall()
    elif 'React.js'==VideoName:
        cursor.execute("SELECT * FROM crawling_video.react_videos")
        data = cursor.fetchall()
    elif 'Vue.js'==VideoName:
        cursor.execute("SELECT * FROM crawling_video.vue_videos")
        data = cursor.fetchall()
    elif 'Angular'==VideoName:
        cursor.execute("SELECT * FROM crawling_video.Angular_videos")
        data = cursor.fetchall()
    elif 'jQuery'==VideoName:
        cursor.execute("SELECT * FROM crawling_video.jQuery_videos")
        data = cursor.fetchall()
    elif 'React Native'==VideoName:
        cursor.execute("SELECT * FROM crawling_video.reactnative_videos")
        data = cursor.fetchall()
    elif '플러터'==VideoName:
        cursor.execute("SELECT * FROM crawling_video.flutter_videos")
        data = cursor.fetchall()
    elif '모의해킹'==VideoName:
        cursor.execute("SELECT * FROM crawling_video.hacker_videos")
        data = cursor.fetchall()
    elif '보안관제'==VideoName:
        cursor.execute("SELECT * FROM crawling_video.cert_videos")
        data = cursor.fetchall()
    elif 'CS지식'==VideoName:
        cursor.execute("SELECT * FROM crawling_video.cs_videos")
        data = cursor.fetchall()

    return Response({'message': data})