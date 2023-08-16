from django.contrib import admin
from .models import bookPost, bookComment, Study, UserRental
from django.utils.html import format_html

# 관리자 페이지에서 관리
# bookPost 관리
class bookPostAdmin(admin.ModelAdmin):
    # list_display는 튜플 형식으로서 전달하기 때문에 마지막에 꼭 ,를 붙여줘야 한다
    list_display = ('title','user','created_at','sell_price','styled_rent_status')

    def styled_rent_status(self, obj):
        # obj : 레코드
        # f string : python 최신 문법
        # 다양한 문자열 연결
        # 1. + 연결 : '<b>'+obj.status + '</b>'
        # 2. % format : '<b>%s</b>'%(obj.status)
        # 3. format 함수 : '<b>{}</b>'.format(obj.status)
        # 4. f-string : f'<b>{obj.status}</b>'
        if obj.rent_state == '대여중':
            return format_html(f'<span style="color:red">{obj.rent_state}</span>')
        return format_html(f'<span">{obj.rent_state}</span>')

    # ModelAdmin 내부에 이미 changelist_view함수가 만들어져 있다
    def changelist_view(self, request, extra_context=None):
        # 우리가 원하는 동작을 하고 그 다음에 원래 만들어져 있는 함수를 호출해라
        extra_context = {'title': '게시물 목록'}
        return super().changelist_view(request, extra_context)


    # 세부적인 페이지 커스텀
    def changeform_view(self, request, object_id, form_url="", extra_context=None):
        if object_id:
            post=bookPost.objects.get(pk=object_id)
            extra_context={'title':f'{post.title} _ {post.user} 게시물 정보 수정하기'}
        return super().changeform_view(request,object_id,form_url,extra_context)

    styled_rent_status.short_description = '대여 상태'



# 대여 기능 관리
class rentAdmin(admin.ModelAdmin):
    # list_display는 튜플 형식으로서 전달하기 때문에 마지막에 꼭 ,를 붙여줘야 한다
    list_display = ('get_book_title','get_book_user','user','rent_start_date','styled_rent_end_date')

    def get_book_title(self, obj):
        return obj.book.title

    def get_book_user(self, obj):
        return obj.book.user

    def styled_rent_end_date(self, obj):
        return format_html(f'<span style="color:red"><b>{obj.rent_end_date}</b></span>')

    # ModelAdmin 내부에 이미 changelist_view함수가 만들어져 있다
    def changelist_view(self, request, extra_context=None):
        # 우리가 원하는 동작을 하고 그 다음에 원래 만들어져 있는 함수를 호출해라
        extra_context = {'title': '대여 목록'}
        return super().changelist_view(request, extra_context)

    # 세부적인 페이지 커스텀
    def changeform_view(self, request, object_id, form_url="", extra_context=None):
        if object_id:
            rental=UserRental.objects.get(pk=object_id)
            extra_context={'title':f'{rental.book.title} _ {rental.book.user} 대여 정보 수정하기'}
        return super().changeform_view(request,object_id,form_url,extra_context)


    styled_rent_end_date.short_description = '반납일'
    get_book_title.short_description='게시물'
    get_book_user.short_description='작성자'

admin.site.register(bookPost,bookPostAdmin)
admin.site.register(bookComment)
admin.site.register(Study)
admin.site.register(UserRental,rentAdmin)

