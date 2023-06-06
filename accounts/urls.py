from allauth.account.views import account_inactive
from dj_rest_auth.registration.views import VerifyEmailView,ConfirmEmailView
from django.urls import path, include, re_path
from accounts.views import ProfileView

urlpatterns = [
    #회원가입
    path('', include('dj_rest_auth.urls')),
    path('registration/', include('dj_rest_auth.registration.urls')),
    path('registration/account_inactive/', account_inactive, name='account_inactive'),
    path('profile/<int:pk>',ProfileView.as_view()),

    # 유효한 이메일이 유저에게 전달
    #re_path(r'^account-confirm-email/$', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    # 유저가 클릭한 이메일(=링크) 확인
    #re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(), name='account_confirm_email'),
]