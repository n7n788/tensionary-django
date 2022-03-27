#Webサイトをログイン必須にするための設定
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseRedirect

class AuthMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        #ログインとユーザー登録のみ、ログインなしでの実行を許可する
        if request.path != '/diary/login' and request.path != '/diary/register_user' and not request.user.is_authenticated:
            return HttpResponseRedirect('/diary/login')
        return response