from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *




urlpatterns=[
    path('recommend',recommend,name='recommend'),

]