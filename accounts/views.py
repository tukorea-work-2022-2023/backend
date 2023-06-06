from rest_framework import generics, status

from accounts.models import Profile
from accounts.serializers import ProfileSerializer

from django.http import HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from allauth.account.models import EmailConfirmation, EmailConfirmationHMAC

#프로필은 조회와 수정 기능만 있으면 되므로 RetrieveUpdateAPIView 사용
class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# class ConfirmEmailView(APIView):
#     permission_classes = [AllowAny]
#
#     def get(self, *args, **kwargs):
#         self.object = confirmation = self.get_object()
#         confirmation.confirm(self.request)
#         # A React Router Route will handle the failure scenario
#         return HttpResponseRedirect('/') # 인증성공
#
#     def get_object(self, queryset=None):
#         key = self.kwargs['key']
#         email_confirmation = EmailConfirmationHMAC.from_key(key)
#         if not email_confirmation:
#             if queryset is None:
#                 queryset = self.get_queryset()
#             try:
#                 email_confirmation = queryset.get(key=key.lower())
#             except EmailConfirmation.DoesNotExist:
#                 # A React Router Route will handle the failure scenario
#                 return HttpResponseRedirect('/') # 인증실패
#         return email_confirmation
#
#     def get_queryset(self):
#         qs = EmailConfirmation.objects.all_valid()
#         qs = qs.select_related("email_address__user")
#         return qs