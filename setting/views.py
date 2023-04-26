from django.shortcuts import render
from home.models import bookPost
from rest_framework.decorators import api_view,permission_classes
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
# Creat
# e your views here.


# 사용자가 최근에 본 게시물
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def currentPost(request,pk):
    user=get_object_or_404(user)
