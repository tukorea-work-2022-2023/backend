from django.core import serializers
from rest_framework import serializers
from account.models import User
from .models import bookPost,bookComment,bookSearch
from taggit.serializers import TaggitSerializer,TagListSerializerField


# 책 등록 게시물들 JSON 형태
class bookPostSerializer(TaggitSerializer,serializers.ModelSerializer):
    user=serializers.ReadOnlyField(source='user.nickname')

    tags=TagListSerializerField()
    class Meta:
        model=bookPost
        fields='__all__'



# 책 등록 게시물 댓글들 JSON 형태
class bookCommentSerializer(serializers.ModelSerializer):
    user=serializers.ReadOnlyField(source='user.nickname')
    class Meta:
        model=bookComment
        fields='__all__'


class bookSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model=bookSearch
        fields='__all__'


