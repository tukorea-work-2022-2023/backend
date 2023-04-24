from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *

urlpatterns = [

    path('video_list/',video_search_list,name='video_search_list'),

]
