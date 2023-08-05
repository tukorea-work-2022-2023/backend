from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *


router=DefaultRouter()

# 전공책 등록 게시물
router.register('majorPost',majorPostViewSet,basename='majorPost')

# 전공책 등록 게시물 댓글
router.register('majorPostComment',majorCommentViewSet,basename='majorPostComment')

# 스캔한 책 정보
router.register('major_bookSearch',major_booksearchViewSet,basename='major_bookSearch')

urlpatterns=router.urls+[
    path('like/<int:pk>/', like_post, name='like_post'),
    path('barcode_bookInfo',barcode_book_info,name='book_Info'),
    path('majorPost/tagged/<str:tag_name>/', MajorListByTag.as_view(), name='major_list_by_tag'),
    path('create_rental/<int:pk>/rent/', create_rental, name='create_rental'),
    path('study/list/<int:major_post_id>/', StudyListByMajorPost.as_view(), name='study-list-by-majorpost')
]