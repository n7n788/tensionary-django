from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register_user', views.register_user, name='register_user'),
    path('edit_diary/<int:num>', views.edit_diary, name='edit_diary'),
    path('create_diary', views.create_diary, name='create_diary'),
    path('setting', views.setting, name='setting'),
    path('setting_email', views.setting_email, name='setting_email'),
    path('setting_password', views.setting_password, name='setting_password'),
]