from django.contrib.auth.models import User # user 모델
from django.contrib.auth.password_validation import validate_password # django 의 패스워드 검증 도구

from rest_framework import serializers
from rest_framework.authtoken.models import Token # token 모델
from rest_framework.validators import UniqueValidator # 이메일 중복 방지를 위한 검증 도구

from django.contrib.auth import authenticate

from account.models import Profile


# django 의 기본 authenticate 함수, 우리가 설정한 DefaultAuthBackend 인 TokenAuth 방식으로
# 유저를 인증해줌.


# 회원가입 시리얼라이저
class RegisterSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())], # 이메일에 대한 중복 검증

    )
    password=serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password], # 비밀번호에 대한 검증
    )

    password2=serializers.CharField(write_only=True,required=True) # 비밀번호 확인을 위한 필드

    class Meta:
        model=User
        fields=('username','password','password2','email')


    # 추가적으로 비밀번호 일치 여부를 확인
    def validate(self,data):
        if data['password']!=data['password2']:
            raise serializers.ValidationError(
                {"password":"Password fields didn't match."}
            )
        return data


    # create  요청에 대하여 create 메소드를 오버라이딩, 유저를 생성하고 토큰을 생성하게 함.
    def create(self, validated_data):
        user=User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()
        token= Token.objects.create(user=user)
        return user


class LoginSerializer(serializers.Serializer):
    username=serializers.CharField(required=True)
    password=serializers.CharField(required=True,write_only=True)
    # write_only 옵션을 통해 클라이언트=>서버 방향의 역직렬화는 가능, 반대는 불가


    def validate(self,data):
        user=authenticate(**data)
        if user:
            token=Token.objects.get(user=user)
            return token

        raise serializers.ValidationError(
            {"error":"Unable to log in with provided credentials."}
        )

# 사용자가 ID/PW를 적어서 보내줬을 때 이를 확인하여
# 그에 해당하는 토큰을 응답하기만 하면 되기 때문에
# ModelSerializer를 사용할 필요가 없다.
class SigninSerializer(serializers.Serializer):
    """"로그인 Serializer"""
    # 비밀번호에 write_only 옵션
    # 클라이언트 -> 서버 역직렬화 가능, 서버 -> 클라이언트 직렬화 불가능
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user:
            return Token.objects.get(user=user)# 로그인 성공 시 토큰 반환
        raise serializers.ValidationError(
            {'error' : 'Unable to sign in with provided credential.'}
        )

class ProfileSerializer(serializers.ModelSerializer):
    """프로필 Serializer"""
    class Meta:
        model = Profile
        fields = ('nickname', 'studentnumber', 'major', 'interest','image')