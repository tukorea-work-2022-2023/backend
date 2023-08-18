import json
from datetime import timedelta
from rest_framework.exceptions import ValidationError
from django.core import serializers
from rest_framework import serializers
from account.models import UserData
from account.serializers import ProfileSerializer
from .models import majorPost,majorComment,Study
from taggit_serializer.serializers import TaggitSerializer,TagListSerializerField
from collections import OrderedDict



# 전공책 등록 게시물 댓글들 JSON 형태
class majorCommentSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = majorComment
        fields = ('pk', 'profile', 'major_post', 'comment','created_at')


class majorCommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = majorComment
        fields = ('major_post', 'comment')



# 전공책 등록 게시물들 JSON 형태
class majorPostSerializer(TaggitSerializer,serializers.ModelSerializer):
    profile=ProfileSerializer(read_only=True)
    comment=majorCommentSerializer(many=True,read_only=True)
    tags = TagListSerializerField(required=False)

    #
    # tags_list = serializers.ListField(
    #     child=serializers.CharField(),
    #     read_only=True
    # )


    class Meta:
        model = majorPost
        fields = (
        'pk', 'profile','category','writer', 'publisher', 'title', 'content', 'image', 'created_at', 'sell_price', 'comment',
        'tags', 'state', 'summary', 'state_image','rent_state','pub_date','hits','rent_start_date','rent_end_date')


    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        instance = super().create(validated_data)
        for tag in tags_data:
            instance.tags.add(tag)
        return instance





class majorPostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = majorPost
        fields = ('category','title', 'writer','publisher','content','image','sell_price','summary','state_image','tags','state','pub_date','rent_start_date','rent_end_date')



class StudySerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    major_post = serializers.PrimaryKeyRelatedField(queryset=majorPost.objects.all())

    class Meta:
        model = Study
        fields = ('pk','profile','major_post', 'study_content', 'created_at', 'headcount','study_period', 'recruit_state')