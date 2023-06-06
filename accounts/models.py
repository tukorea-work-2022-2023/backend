from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    username = models.CharField
    email = models.EmailField(_('email address'), unique=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                primary_key=True)  # 일대일
    nickname = models.CharField(max_length=128)
    studentnumber = models.CharField(max_length=128, null=True, default='')
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
