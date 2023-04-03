import json

from rest_framework.exceptions import ValidationError
from django.core import serializers
from rest_framework import serializers
from account.models import User
from account.serializers import ProfileSerializer
from .models import majorPost,majorComment
from taggit_serializer.serializers import TaggitSerializer,TagListSerializerField



# 책 등록 게시물 댓글들 JSON 형태
class majorCommentSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = majorComment
        fields = ('pk', 'profile', 'major_post', 'comment','created_at')


class majorCommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = majorComment
        fields = ('major_post', 'comment')



# 책 등록 게시물들 JSON 형태
class majorPostSerializer(TaggitSerializer,serializers.ModelSerializer):
    profile=ProfileSerializer(read_only=True)
    comment=majorCommentSerializer(many=True,read_only=True)
    tags= TagListSerializerField()

    class Meta:
        model=majorPost
        fields=('pk','profile','author','publisher','title','content','image','created_at','sell_price','comment','tags','major','class_name')



class majorPostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = majorPost
        fields = ('title', 'author','publisher','content','image','sell_price','summary','state','state_image','major','class_name')



