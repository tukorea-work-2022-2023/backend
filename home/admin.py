from django.contrib import admin
from .models import bookPost, bookComment, Study, UserRental

# 관리자 페이지에서 관리
admin.site.register(bookPost)
admin.site.register(bookComment)
admin.site.register(Study)
admin.site.register(UserRental)