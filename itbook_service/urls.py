from django.contrib import admin
from django.urls import path,include
from home import urls


urlpatterns = [

    #관라자 페이지
    #path("admin/", admin.site.urls),

    #restframework 관리자 페이지
    path('api-auth/', include('rest_framework.urls')),

    #채팅 탭 페이지
    path("chat/", include('chat.urls')),

    #강의 탭 페이지
    path("class/",include('class.urls')),

    #홈화면 탭 페이지
    path("home/", include('home.urls')),

    #전공 탭 페이지
    path("major/",include('major.urls')),

    #환경설정 탭 페이지
    path("setting/",include('setting.urls')),

]
