from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from functools import wraps
from functools import wraps
from functools import wraps

from test01 import settings
from test01 import settings
from test01 import settings

# Create your views here.


def checkLogin(func):
# def checkLogin(func):
# def checkLogin(func):

    """
    检测是否登录
    :param func:
    :return:
    """
    @wraps(func)
    # @wraps(func)
    # @wraps(func)
    def inner(request, *args, **kwargs):
    # def inner(request, *args, **kwargs):
    # def inner(request, *args, **kwargs):
        # 获取当前页面的uri
        referer = request.get_full_path()
        # referer = request.get_full_path()
        # referer = request.get_full_path()
        # print(request.get_full_path())  # /app02/index/ # http://127.0.0.1:8000/app02/login/?next_url=/app02/index/
        # 在视图函数执行之前，先判断下是否登录
        if request.session.get('is_login'):
        # if request.session.get('is_login'):
        # if request.session.get('is_login'):
            return func(request, *args, **kwargs)
            # return func(request, *args, **kwargs)
            # return func(request, *args, **kwargs)
        else:
        # else:
        # else:
            return redirect('/app02/login/?next_url='+referer)
            # return redirect('/app02/login/?next_url='+referer)
            # return redirect('/app02/login/?next_url='+referer)
    return inner
    # return inner
    # return inner


# @csrf_exempt  # 设置post提交时不进行csrf验证   csrf_protect 设置csrf验证

# def login(request):
def login(request):
    # 判断登录
    # if request.method == 'POST':
    if request.method == 'POST':
        # username = request.POST.get('username')
        username = request.POST.get('username')
        # pwd = request.POST.get('pwd')
        pwd = request.POST.get('pwd')
        # 判断用户名和密码
        # if username == 'admin' and pwd == 'admin888':
        if username == 'admin' and pwd == 'admin888':
            # 获取来源页
            # referer = request.GET.get('next_url')
            referer = request.GET.get('next_url')
            # if not referer:
            if not referer:
                # referer = '/app02/index/'
                referer = '/app02/index/'
            # 决定跳转页面
            # res = redirect(referer)
            res = redirect(referer)
            # print(res, type(res))
            # print(res, type(res))
            # 登录成功以后种个标识到客户端
            # 设置session
            # request.session['is_login'] = username
            request.session['is_login'] = username
            # 设置session的过期时间
            # request.session.set_expiry(10)  # 单位秒
            request.session.set_expiry(10)

            # return res
            return res

    # return render(request, 'app02/login.html')
    return render(request, 'app02/login.html')

# def loginOut(request):
def loginOut(request):
    """
    退出
    :param request:
    :return:
    """
    # red = redirect('/app02/login/')
    red = redirect('/app02/login/')
    # 删除指定键的Session
    # red.delete_cookie('is_login')
    # red.delete_cookie('is_login')    # 删除cookie中的字段
    # del request.session['is_login']  # 不会结束会话（sessionid不会被删除），只结束了登录的状态判断
    # del request.session['is_login']
    request.session.delete()   # 删除当前会话的所有数据，sessionid不会删除，当下次再登录时会生成一个新的sessionid 覆盖当前sessionid
    # request.session.delete()
    # 清除过期的会话数据
    request.session.clear_expired()
    # request.session.clear_expired()
    # return red
    return red

# @checkLogin
# @checkLogin
@checkLogin
def index(request):
# def index(request):
# def index(request):
    # # 从请求对象中获取session值
    # username = request.session.get('is_login', None)
    # username = request.session.get('is_login', None)
    # username = request.session.get('is_login', None)
    # print(request.session.__dict__)
    # print(request.session.__dict__, '*'*8)
    # print(request.session.__dict__, '*'*8)
    # {'serializer': <class 'django.core.signing.JSONSerializer'>, 'model': <class 'django.contrib.sessions.models.Session'>, 'accessed': True, 'modified': False, '_SessionBase__session_key': 'd41leotiw7gs4aace44iklpjs755w04x', '_session_cache': {'_session_expiry': 10, 'is_login': 'admin'}}
    # if not username:
    # if not username:
    # if not username:
    #     return redirect('/app02/login/')
    #     return redirect('/app02/login/')
    #     return redirect('/app02/login/')
    # print(request.session.session_key)
    # print(request.session.session_key, '*'*8)   # l2zs1amsf4vzlcwcvym5zlxybidxjepr
    # print(request.session.session_key)
    # return HttpResponse('后台首页，欢迎'+request.session.get('is_login', None)+'来到后台！<a href="/app02/loginOut/">退出</a>')
    # return HttpResponse('后台首页，欢迎'+request.session.get('is_login', None)+'来到后台！<a href="/app02/loginOut/">退出</a>')
    return HttpResponse('后台首页，欢迎'+request.session.get('is_login', None)+'来到后台！<a href="/app02/loginOut/">退出</a>')