import email
from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.email

class Diary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tension = models.IntegerField()
    detail = models.CharField(max_length=200)
    date = models.DateField()
    def __str__(self):
        return str(self.user.email) + '(' + str(self.date) + ')'