import json

from django.contrib.auth.models import User # user 모델
from django.contrib.auth.password_validation import validate_password # django 의 패스워드 검증 도구

from rest_framework import serializers
from rest_framework.authtoken.models import Token # token 모델
from rest_framework.validators import UniqueValidator # 이메일 중복 방지를 위한 검증 도구

from django.contrib.auth import authenticate

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from account.models import Profile, UserData
from statuscode import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ["email", "name", "password"]


    def create(self, validated_data):
        user = UserData.objects.create(email=validated_data['email'],
                                       name=validated_data['name']
                                       )

        user.set_password(validated_data['password'])
        user.save()
        return user



class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):

        od1 = json.dumps(attrs)
        od2 = json.loads(od1)

        name = UserData.objects.filter(email=od2['email']).first()

        if name:
            if not name.check_password(od2['password']):

                data1 = VAILDPASSWORD
                return data1

            else:
                data = {}
                user_id = name.pk
                refresh = RefreshToken.for_user(name)
                new_data = {
                    'user_id': user_id,
                    'refresh': str(refresh),
                    'access': str(refresh.access_token)
                }
                data.update(new_data)


        else:

            data1 = VAILDEMAIL
            return data1


        return data




class ProfileSerializer(serializers.ModelSerializer):
    """프로필 Serializer"""
    interest = serializers.ListField(child=serializers.CharField(), write_only=True)
    class Meta:
        model = Profile
        fields = ('user','nickname', 'studentnumber', 'major', 'interest', 'image')