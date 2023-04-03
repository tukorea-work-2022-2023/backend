from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *


router=DefaultRouter()

# 책 등록 게시물
router.register('majorPost',majorPostViewSet,basename='majorPost')

# 책 등록 게시물 댓글
router.register('majorPostComment',majorCommentViewSet,basename='majorPostComment')

# 스캔한 책 정보
router.register('majorSearch',majorSearchViewSet,basename='majorSearch')

urlpatterns=router.urls+[
    path('majorPost/like/<int:pk>/', like_post, name='like_post')
]
