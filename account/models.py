from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                primary_key=True)  # 일대일
    nickname = models.CharField(max_length=128)
    studentnumber = models.CharField(max_length=128,null=True,default='')
    major = models.CharField(max_length=128)
    interest = models.CharField(max_length=128)
    image = models.ImageField(upload_to='profile/', default='default.png')


# 1. User 모델이 post_save 이벤트를 발생시켰을 때
# 2. 해당 이벤트의 발생 여부를 인지하고
# 3. 해당 User 인스턴스와 연결되는 프로필 데이터를 생성함
# @receiver는 User 생성 이벤트를 감지하여 프로필을 자동으로 생성한다.
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)