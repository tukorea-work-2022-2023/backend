from django.contrib.auth.base_user import BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import AbstractUser
from django.db import models


class UserManager(BaseUserManager):
    use_in_migration = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is Required')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')

        return self.create_user(email, password, **extra_fields)


class UserData(AbstractUser):
    username = None
    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length=100, unique=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)


    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'users_userdata'
        ordering = ['name']  # 'ordering' 속성을 'name' 필드로 수정
class Profile(models.Model):
    user = models.OneToOneField(UserData, on_delete=models.CASCADE,
                                primary_key=True)  # 일대일
    nickname = models.CharField(max_length=128)
    studentnumber = models.CharField(max_length=128,null=True,default='')
    major = models.CharField(max_length=128)
    interest = models.TextField(max_length=128)
    image = models.ImageField(upload_to='profile/', default='default.png')


# 1. User 모델이 post_save 이벤트를 발생시켰을 때
# 2. 해당 이벤트의 발생 여부를 인지하고
# 3. 해당 User 인스턴스와 연결되는 프로필 데이터를 생성함
# @receiver는 User 생성 이벤트를 감지하여 프로필을 자동으로 생성한다.
@receiver(post_save, sender=UserData)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)