from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


from account.models import Profile, UserData


# User와 Profile은 서로 연관된 모델이지만
# Admin 페이지에서는 분리된 테이블로 보이는 것을 개선
#class ProfileInline(admin.StackedInline):
#    model = Profile
#    can_delete = False
#    verbose_name_plural = 'profile'



# majorPost 관리
class ProfileAdmin(admin.ModelAdmin):
    # list_display는 튜플 형식으로서 전달하기 때문에 마지막에 꼭 ,를 붙여줘야 한다
    list_display = ('user','nickname', 'studentnumber', 'major', 'interest', 'image')


    # ModelAdmin 내부에 이미 changelist_view함수가 만들어져 있다
    def changelist_view(self, request, extra_context=None):
        # 우리가 원하는 동작을 하고 그 다음에 원래 만들어져 있는 함수를 호출해라
        extra_context = {'title': '회원 프로필 목록'}
        return super().changelist_view(request, extra_context)


    # 세부적인 페이지 커스텀
    def changeform_view(self, request, object_id, form_url="", extra_context=None):
        if object_id:
            profile=Profile.objects.get(pk=object_id)
            extra_context={'title':f'{profile.user} _ {profile.studentnumber} 프로필 정보 수정하기'}
        return super().changeform_view(request,object_id,form_url,extra_context)

class UserAdmin(admin.ModelAdmin):
    # list_display는 튜플 형식으로서 전달하기 때문에 마지막에 꼭 ,를 붙여줘야 한다
    list_display = ('email', 'name', 'is_admin', 'created_at', 'updated_at', 'is_active')

    # ModelAdmin 내부에 이미 changelist_view함수가 만들어져 있다
    def changelist_view(self, request, extra_context=None):
        # 우리가 원하는 동작을 하고 그 다음에 원래 만들어져 있는 함수를 호출해라
        extra_context = {'title': '회원 목록'}
        return super().changelist_view(request, extra_context)

    # 세부적인 페이지 커스텀
    def changeform_view(self, request, object_id, form_url="", extra_context=None):
        if object_id:
            userdata = UserData.objects.get(pk=object_id)
            extra_context = {'title': f'{userdata.email} _ {userdata.name} 회원 정보 수정하기'}
        return super().changeform_view(request, object_id, form_url, extra_context)


admin.site.register(Profile, ProfileAdmin)
admin.site.register(UserData, UserAdmin)

