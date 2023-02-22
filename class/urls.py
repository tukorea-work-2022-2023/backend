from django.contrib import admin
from django.urls import path,include
from .views import class_crawling

urlpatterns = [

    path('/<String:search>/', class_crawling, name='class_crawling')

]
