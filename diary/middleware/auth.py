#Webサイトをログイン必須にするための設定
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseRedirect

class LoginRequiredMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        #ログインとユーザー登録、管理画面のみログインなしでの実行を許可する
        if request.path != '/diary/login' and request.path != '/diary/register_user' and \
           request.path != '/admin/login/' and \
           request.path != '/admin/' and not request.user.is_authenticated:
            return HttpResponseRedirect('/diary/login')
        return response