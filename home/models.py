from django.db import models
from django.urls import reverse
from account.models import User
#from users.models import User
from taggit.managers import TaggableManager #태그 기능을 함

class bookPost(models.Model):

    # 1. 책 등록게시물의 id 값
    id = models.AutoField(primary_key=True,null=False,blank=False)

    # 2. 제목
    title=models.CharField(max_length=100)

    # 3. 작가
    author=models.CharField(max_length=100)

    # 4. 출판사
    publisher=models.CharField(max_length=100)

    # 5. 작성일
    created_at = models.DateTimeField(auto_now_add=True)

    # 6. 작성자
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    # 7. 본문
    content = models.TextField()

    # 8. 조회수
    hits = models.PositiveIntegerField(default=0)

    # 9. 태그
    tags=TaggableManager(blank=True)


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
