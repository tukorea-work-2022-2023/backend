from rest_framework import serializers
from accounts.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    """프로필 Serializer"""
    interest = serializers.ListField(child=serializers.CharField(), write_only=True)
    class Meta:
        model = Profile
        fields = ('nickname', 'studentnumber', 'major', 'interest','image')