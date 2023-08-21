from django.db import models
from django.urls import reverse
from account.models import UserData,Profile
from taggit.managers import TaggableManager #태그 기능을 함
from django.utils import timezone

class bookPost(models.Model):


    # 1. 책 제목
    title=models.CharField(max_length=128, verbose_name ="책 제목")

    # 2. 책 작가
    writer = models.CharField(max_length=100, verbose_name ="책 작가")

    # 3. 출판사
    publisher=models.CharField(max_length=100, verbose_name ="출판사")

    # 5. 생성 일자
    created_at = models.DateTimeField(auto_now_add=True, verbose_name ="생성 일자")

    # 6. 작성자
    user = models.ForeignKey(UserData, null=True, blank=True, on_delete=models.CASCADE, related_name='book_posts',
                         verbose_name ="작성자")

    # 7. 책 설명
    content = models.TextField(verbose_name ="책 설명")

    # 8. 조회수
    hits = models.PositiveIntegerField(default=0, verbose_name ="조회수")

    # 9. 태그
    tags=TaggableManager(verbose_name ="태그",blank=True)

    # 10. 책 이미지
    image = models.ImageField(upload_to='post/', default='default.png')

    # 11. 대여 금액
    sell_price=models.IntegerField(default=0, verbose_name = "대여 금액")


    # 12. 책 요약
    summary = models.TextField(null=False,default = '' ,verbose_name="책 요약")

#choices=BOOK_STATE,
    # 13. 책 상태
    state= models.CharField(max_length=100, verbose_name ="책 상태")


    # 14. 카테고리
    #category_id=models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE, related_name='book_posts',
     #                        verbose_name ="카테고리")

    # 15. 찜
    like = models.ManyToManyField(UserData)


    # 16. 책 상태 사진
    state_image = models.FileField(upload_to='state_images/',verbose_name="책 상태 사진")

    # 17. profile
    profile=models.ForeignKey(Profile,null=False,default = '' ,on_delete=models.CASCADE,blank=True)


    # 18. 책 대여상태
    rent_state = models.CharField(null=False,default = '대여 가능' ,max_length=100, verbose_name="책 대여상태")

    # 19. 출판일
    pub_date = models.CharField(null=False, default='', max_length=100, verbose_name="출판일")

    # 20. 대여 시작 일자
    rent_start_date = models.DateField(null=True,verbose_name="대여 시작 일자")

    # 21. 대여 끝난 일자
    rent_end_date = models.DateField(null=True,verbose_name="대여 끝난 일자")



    #tags_list = models.CharField(max_length=100,blank=True)

    # 조회 할 때마다 업데이트
    @property
    def update_counter(self):
        self.hits = self.hits + 1
        self.save()




# 댓글 달기
class bookComment(models.Model):
    book_post=models.ForeignKey(bookPost,related_name='comments',null=False,blank=False,on_delete=models.CASCADE)
    user=models.ForeignKey(UserData,null=False,blank=False,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, null=False,default = '' ,on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True, null=False, blank=False)
    comment = models.TextField()

    class Meta:
        db_table = 'book_comment'


# 스터디
class Study(models.Model):
    book_post=models.ForeignKey(bookPost,related_name='study',null=False,blank=False,on_delete=models.CASCADE)
    user=models.ForeignKey(UserData,null=False,blank=False,on_delete=models.CASCADE,verbose_name ="생성자")
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True, null=False, blank=False,verbose_name ="생성 일자")
    headcount = models.PositiveIntegerField(default=0, verbose_name ="스터디 인원")
    study_period = models.IntegerField(verbose_name ="스터디 기간")
    study_content = models.TextField(null=False,default = '',verbose_name="스터디 설명")
    recruit_state = models.CharField(null=False, default='모집중', max_length=100, verbose_name="스터디 모집 상태")
    class Meta:
        db_table = 'study'

# 대여 일수
class UserRental(models.Model):
    user = models.ForeignKey(UserData, on_delete=models.CASCADE,verbose_name="대여자")
    book = models.ForeignKey(bookPost, on_delete=models.CASCADE)
    rent_start_date = models.DateField(default=timezone.now,verbose_name="대여 시작일")
    rent_end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"