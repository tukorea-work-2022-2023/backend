from django.urls import path
from account.views import RegisterView
from account.views import SigninView
from account.views import ProfileView

urlpatterns = [
    #회원가입
    path('signup/',RegisterView.as_view()),
    path('signin/',SigninView.as_view()),
    path('profile/<int:pk>',ProfileView.as_view()),
]