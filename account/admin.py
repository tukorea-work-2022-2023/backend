from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


from account.models import Profile, UserData


# User와 Profile은 서로 연관된 모델이지만
# Admin 페이지에서는 분리된 테이블로 보이는 것을 개선
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    ordering = ['name']


admin.site.register(UserData, UserAdmin)

