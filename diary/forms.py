from django import forms

from diary.models import Diary, User

from django.contrib.auth.forms import PasswordChangeForm

class LoginUserForm(forms.Form):
    email = forms.EmailField(label='メールアドレス')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput(), min_length=8)

class RegisterUserForm(forms.Form):
    email = forms.EmailField(label='メールアドレス')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput(), min_length=8)
    password_again = forms.CharField(label='パスワード(確認)', widget=forms.PasswordInput(), min_length=8)

class DiaryForm(forms.ModelForm):
    tension = forms.IntegerField(
        label='今日の気分', max_value=5, min_value=0,
        required=False,
        widget=forms.TextInput(attrs={
            'type': 'range',
            'class': 'slider',
            'min': '0',
            'max': '100',
            'id': 'myTension',
            'step': 1})
    )
    detail = forms.CharField(label='コメント',
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'textarea',
            'placeholder': 'コメントを書く'}))
    class Meta:
            model = Diary
            fields = ('tension', 'detail')

class SettingEmailForm(forms.ModelForm):
    email = forms.EmailField(
        label='メールアドレス'
    )
    class Meta:
        model = User
        fields = ['email']

# class SettingPasswordForm(forms.Form):
    # current_password = forms.CharField(label='現在のパスワード', widget=forms.PasswordInput(), min_length=8)
    # password = forms.CharField(label='パスワード', widget=forms.PasswordInput(), min_length=8)
    # password_again = forms.CharField(label='パスワード(確認)', widget=forms.PasswordInput(), min_length=8)

class SettingPasswordForm(PasswordChangeForm):
    """パスワード変更フォーム"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'