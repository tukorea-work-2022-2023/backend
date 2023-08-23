import json
import random
from datetime import datetime, timedelta

import jwt
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import generics, status, serializers
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from account.models import Profile, UserData
from account.serializers import UserSerializer, ProfileSerializer
from itbook_service import settings
from statuscode import *


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if not serializer.validated_data['email'].endswith('ac.kr'):
            raise serializers.ValidationError({'email': ['이메일 형식이 올바르지 않습니다.']})
            # 이메일 인증 코드를 생성합니다.
        verification_code = random.randint(100000, 999999)
        def send_email_verification_code(email,verification_code):
            # 이메일 인증 코드를 사용자의 이메일로 전송합니다.
            send_mail(
                '[이메일 인증 코드]',
                '이메일 인증 코드는 {}입니다.'.format(verification_code),
                'from@example.com',
                [email],
            )

        email = serializer.validated_data['email']
        send_email_verification_code(email, verification_code)

        # 회원 정보를 저장합니다.
        user = UserData.objects.create_user(
            email=email,
            password=serializer.validated_data['password'],
            verification_code=verification_code,
            is_active=False,
        )

        # 회원 인증 코드를 저장합니다.
        user.verification_code = verification_code

        return Response({
            'message': '이메일 인증 코드를 전송했습니다.'
        })

# 이메일 인증 API 뷰를 추가합니다.
class VerifyEmailView(APIView):
    def post(self, request):
        verification_code = request.data['verification_code']

        # 유효한 회원 인증 코드인지 확인합니다.
        if not verification_code:
            raise serializers.ValidationError({'verification_code': ['필수 항목입니다.']})

        if verification_code is None:
            raise TypeError('verification_code should not be None.')

        user = UserData.objects.filter(verification_code=verification_code).first()
        if not user:
            return Response({
                'message': '유효한 인증 코드가 아닙니다.'
            }, status=status.HTTP_400_BAD_REQUEST)

        # 회원 인증 코드를 제거합니다.
        user.verification_code = None
        user.is_active = True
        user.save()

        return Response({
            'message': '회원 인증이 완료되었습니다.'
        })


from .serializers import CustomTokenObtainPairSerializer

from rest_framework_simplejwt.views import TokenObtainPairView


class CustomTokenObtainPairView(TokenObtainPairView):
    # Replace the serializer with your custom

    serializer_class = CustomTokenObtainPairSerializer

    def delete(self, request):
        # 쿠키에 저장된 토큰 삭제 => 로그아웃 처리
        response = Response({
            "message": "Logout success"
        }, status=status.HTTP_202_ACCEPTED)
        response.delete_cookie("access")
        response.delete_cookie("refresh")
        return response



#프로필은 조회와 수정 기능만 있으면 되므로 RetrieveUpdateAPIView 사용
class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


# 이메일 인증
# 회원가입 후 이메일 인증 토큰 생성과 이메일 전송
