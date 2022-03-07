from django.shortcuts import redirect, render

from diary.forms import DiaryForm, LoginUserForm, RegisterUserForm, SettingEmailForm, SettingPasswordForm

#ログインに必要な関数
from django.contrib.auth import login
from .models import User
# Create your views here.
'''
トップページ
  * 日記の新規作成
'''
def index(request):
    params = {
        'title': 'Tensionary',
    }
    return render(request, 'diary/index.html', params)

'''
日記新規作成
'''
def create_diary(request):
    params = {
        'title': 'Create Diary',
        'form': DiaryForm(),
    }
    if (request.method == 'POST'):
        # ここで入力内容の照合
        print("Tension: " + request.POST['tension'] + '\n' + "Detail: " + request.POST['detail'])
        return redirect(to='/diary')
    return render(request, 'diary/create_diary.html', params)

'''
日記編集
'''
def edit_diary(request, num):
    params = {
        'title': 'Edit Diary',
        'form': DiaryForm(),
    }
    if (request.method == 'POST'):
        # ここで入力内容の照合
        return redirect(to='/diary')
    return render(request, 'diary/edit_diary.html', params)

'''
設定画面
'''
def setting(request):
    params = {
        'title': 'Setting',
    }
    return render(request, 'diary/setting.html', params)

def setting_email(request):
    params = {
        'title': 'Setting Password',
        'form': SettingEmailForm(),
    }
    return render(request, 'diary/setting_email.html', params)

def setting_password(request):
    params = {
        'title': 'Setting Password',
        'form': SettingPasswordForm(),
    }
    return render(request, 'diary/setting_password.html', params)

'''
ログイン
  * DBと照合
  * OKならトップページへ遷移
'''
#この関数の内部でDjango標準のlogin関数を利用するため、関数名を変更した
def login_user(request):
    
    error_message = '' 
    form = RegisterUserForm()
    
    if (request.method == 'POST'):
        # ここで入力内容の照合
        email = request.POST['email']
        password = request.POST['password']
        
        #メールアドレスが一致するユーザーを検索
        user = User.objects.get(email=email)
        #そのユーザーが存在し、パスワードが一致していたらログイン
        if user is not None and user.password == password:
            login(request, user)
            return redirect(to='/diary')
        else:
            #認証失敗したので、エラーメッセージを設定
            error_message = 'メールアドレスまたはパスワードが間違っています'
            form = RegisterUserForm(request.POST)
            
    params = {
        'title': 'Register User',
        'form': form,
        'error_message': error_message,
    }
    return render(request, 'diary/login.html', params)
'''
新規登録
  * POST送信されたユーザー名, パスワードを取得しDB登録
  * 今日の日付, ログインユーザーをDB登録

  * emailがDBに登録済みかどうか確認
  * パスワードとパスワード(確認)が一致するか確認
        -> OKならDB登録
        -> NGならエラーメッセージだして再入力

  * 登録完了したらログイン画面にリダイレクト
'''
def register_user(request):
    if (request.method == 'POST'):
        # ここで登録内容チェック
        return redirect(to='/diary/login')

    params = {
        'title': 'Register User',
        'form': RegisterUserForm(),
    }
    return render(request, 'diary/register_user.html', params)
