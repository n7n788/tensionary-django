import email
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=100)#通常のユーザーは利用しない
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'#ログイン時に要求されるユーザー名をメアドに変更
    REQUIRED_FIELDS = ['username']#管理ユーザーは新規登録でユーザー名を入力する必要がある
    
    #Django標準のユーザーと重複利用されるのを防ぐ
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
    
    def __str__(self):
        return self.email

class Diary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tension = models.IntegerField()
    detail = models.CharField(max_length=500)
    date = models.DateField()
    def __str__(self):
        return str(self.user.email) + '(' + str(self.date) + ')'