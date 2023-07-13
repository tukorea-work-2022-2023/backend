from django.shortcuts import render
from home.models import bookPost
from account.models import User,Profile
from home.serializers import bookPostSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response



# 사용자의 관심사 기반 추천 게시물 출력
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommend(request):
    bookposts=[]
    # get 요청한 사용자의 profile을 가져옴.
    profile = Profile.objects.get(user=request.user)

    #tags=book_posts.tags
    # for post in book_posts:
    #     print(post.tags.all())
    # #print(book_posts)

    #배열로 반환
    interest = profile.interest
    interest = eval(interest)

    #print(interest[0])
    #print(len(interest))
    if len(interest)>0:
        for i in interest:
            filtered_posts=bookPost.objects.filter(tags__name=i)
            #print(filtered_posts)
            bookposts.extend(filtered_posts)

        serializer = bookPostSerializer(bookposts, many=True)
        return Response(serializer.data)