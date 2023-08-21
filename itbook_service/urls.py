from django.contrib import admin
from baton.autodiscover import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from home import urls
from chat import routing


urlpatterns = [


    #관라자 페이지
    path("admin/", admin.site.urls),

    #관리자페이지 테마
    path("baton/", include('baton.urls')),

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

    #회원가입/로그인 탭 페이지
    path("account/",include('account.urls')),

    *routing.websocket_urlpatterns,


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


