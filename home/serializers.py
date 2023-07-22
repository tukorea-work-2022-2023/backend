import json
from datetime import timedelta

from rest_framework.exceptions import ValidationError
from django.core import serializers
from rest_framework import serializers
from account.models import UserData
from account.serializers import ProfileSerializer
from .models import bookPost, bookComment, Study
from taggit_serializer.serializers import TaggitSerializer,TagListSerializerField
from collections import OrderedDict



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



# 책 등록 게시물들 JSON 형태
class bookPostSerializer(TaggitSerializer,serializers.ModelSerializer):
    profile=ProfileSerializer(read_only=True)
    comment=bookCommentSerializer(many=True,read_only=True)
    tags = TagListSerializerField(required=False)

    class Meta:
        model = bookPost
        fields = (
        'pk', 'profile', 'writer', 'publisher', 'title', 'content', 'image', 'created_at', 'sell_price', 'comment',
        'tags', 'state', 'summary', 'state_image','rent_state','pub_date','hits','rent_start_date','rent_end_date')


    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        instance = super().create(validated_data)
        for tag in tags_data:
            instance.tags.add(tag)
        return instance



class bookPostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = bookPost
        fields = ('title', 'writer','publisher','content','image','sell_price','summary','state_image','tags','state','pub_date','rent_start_date','rent_end_date')


# 스터디 게시물

class StudySerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    book_post = serializers.PrimaryKeyRelatedField(queryset=bookPost.objects.all())

    class Meta:
        model = Study
        fields = ('pk','profile','book_post', 'study_content', 'created_at', 'headcount','study_period', 'recruit_state')


