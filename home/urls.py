from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *


router=DefaultRouter()

# 책 등록 게시물
router.register('bookPost',bookPostViewSet,basename='bookPost')

# 책 등록 게시물 댓글
router.register('bookPostComment',bookCommentViewSet,basename='bookPostComment')

# 스캔한 책 정보
router.register('bookSearch',bookSearchViewSet,basename='bookSearch')



urlpatterns=router.urls+[
    path('like/<int:pk>/', like_post, name='like_post'),
    path('barcode_bookInfo',barcode_book_info,name='book_Info'),
    path('bookPost/tagged/<str:tag_name>/', BookListByTag.as_view(), name='book_list_by_tag'),
    path('mypage/',MyPageView.as_view(),name='mypage'),
    path('mylike/',LikeListByUser.as_view(),name='mylike'),
    path('my_rent/', my_rental_detail, name='my-rent'),
    path('create_rental/<int:pk>/rent/', create_rental, name='create_rental'),

]