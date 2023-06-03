from django.shortcuts import render
from home.models import bookPost
from account.models import User,Profile
from home.serializers import bookPostSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated



# 사용자가 최근에 본 게시물
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def currentPost(request,pk):
#     user=get_object_or_404(user)


# 사용자의 관심사 기반 추천 게시물 출력
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommend(request):
    profile = Profile.objects.get(user=request.user)
    interest=profile.interest
    if len(interest)>0:
        for i in range(len(interest)):
            if interest[i] in bookPost.tags:
                interest_post=bookPost.objects.filter(tags__name=interest[i])
                serializer=bookPostSerializer(interest_post,many=True)
                return Response(serializer.data)

