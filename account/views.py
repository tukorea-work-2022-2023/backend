from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import generics, status

from account.models import Profile
from account.serializers import RegisterSerializer, ProfileSerializer
from account.serializers import SigninSerializer

# 회원가입은 생성기능 post만 있기 때문에 CreateAPIView만 사용
class RegisterView(generics.CreateAPIView):
    """회원가입: POST"""
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

# - 로그인은 모델과 관련이 없기 때문에 기본 `GenericAPIView`를 사용
# - 1차적인 보안을 위해 `POST` 요청만을 처리, 로그인 성공 시 토큰 반환
class SigninView(generics.GenericAPIView):
    """"로그인 : post"""
    serializer_class = SigninSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data # validate()의 return 값
        return Response({'token' : token.key}, status=status.HTTP_200_OK)

#프로필은 조회와 수정 기능만 있으면 되므로 RetrieveUpdateAPIView 사용
class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
