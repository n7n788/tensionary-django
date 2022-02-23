from django.contrib import admin

from diary.models import Diary, User

# Register your models here.
admin.site.register(User)
admin.site.register(Diary)