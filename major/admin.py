from django.contrib import admin
from .models import majorPost, majorComment, Study, UserRental

# 관리자 페이지에서 관리
admin.site.register(majorPost)
admin.site.register(majorComment)
admin.site.register(Study)
admin.site.register(UserRental)