from django.core import serializers
from rest_framework import serializers
from account.models import User
from .models import bookPost,bookComment,bookSearch
from taggit.serializers import TaggitSerializer,TagListSerializerField


# 책 등록 게시물들 JSON 형태
class bookPostSerializer(TaggitSerializer,serializers.ModelSerializer):
    profile=ProfileSerializer(read_only=True)

    class Meta:
        model=bookPost
        fields=('pk','profile','author','publisher','title','content','image','created_at','sell_price','')


class bookPostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = bookPost
        fields = ('title', 'author','publisher','content','image','sell_price','summary','state','category_id','state_image')






# 책 등록 게시물 댓글들 JSON 형태
class bookCommentSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = bookComment
        fields = ('pk', 'profile', 'book_post', 'comment','created_at')


class bookCommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = bookComment
        fields = ('book_post', 'comment')


class bookSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model=bookSearch
        fields='__all__'


