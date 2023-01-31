from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *


router=DefaultRouter()

# 책 등록 게시물
router.register('bookPost',bookPostViewSet,basename='bookPost')

# 책 등록 게시물 댓글
router.register('bookPostComment',bookPostViewSet,basename='bookPostComment')

# 스캔한 책 정보
router.register('bookSearch',bookSearchViewSet,basename='bookSearch')

urlpatterns=[
    path('',include(router.urls))
]