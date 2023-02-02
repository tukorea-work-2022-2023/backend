from django.db import models
from django.urls import reverse
from account.models import User
#from users.models import User
from taggit.managers import TaggableManager #태그 기능을 함

class bookPost(models.Model):

    # 1. 책 등록 게시물의 id
    book_id = models.AutoField(primary_key=True, null=False, blank=False,
                               verbose_name = "책 등록 게시물 id")

    # 2. 책 제목
    title=models.CharField(max_length=100, verbose_name ="책 제목")

    # 3. 책 작가
    author=models.CharField(max_length=100, verbose_name ="책 작가")

    # 4. 출판사
    publisher=models.CharField(max_length=100, verbose_name ="출판사")

    # 5. 생성 일자
    created_at = models.DateTimeField(auto_now_add=True, verbose_name ="생성 일자")

    # 6. 작성자
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE,
                             verbose_name ="작성자")

    # 7. 책 설명
    content = models.TextField(verbose_name ="책 설명")

    # 8. 조회수
    hits = models.PositiveIntegerField(default=0, verbose_name ="조회수")

    # 9. 태그
    tags=TaggableManager(blank=True, verbose_name ="태그")

    # 10. 책 이미지



    # 11. 대여 금액
    sell_price=models.IntegerField(default=0, verbose_name = "대여 금액")


    # 12. 책 요약

    # 13. 책 상태





    # 14. 카테고리
   # category_id=models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE,
     #                        verbose_name ="카테고리")


    # 15. 댓글
    book_review_id=models.ForeignKey(bookComment, null=True, blank=True, on_delete=models.CASCADE,verbose_name ="댓글")



    # 16. 스터디
    # book_study_id=models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE,
    #                         verbose_name ="스터디")





    # 조회 할 때마다 업데이트
    def update_counter(self):
        self.hits = self.hits + 1
        self.save()







# 댓글 달기
class bookComment(models.Model):
    id= models.AutoField(primary_key=True, null=False, blank=False)
    book_post=models.ForeignKey(bookPost,null=False,blank=False,on_delete=models.CASCADE)
    user=models.ForeignKey(User,null=False,blank=False,on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True, null=False, blank=False)
    comment = models.TextField()

    def __str__(self):
        return self.comment



class bookSearch(models.Model):

    title=models.CharField(max_length=100)

    author=models.CharField(max_length=100)

    publisher=models.CharField(max_length=100)

    pub_date=models.CharField(max_length=100)

    description = models.TextField()

    def __str__(self):
        return self.bookSearch
