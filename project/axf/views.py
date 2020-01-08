from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from .models import Wheel, Nav, Mustbuy, Foodtypes, Goods, User

# register用的，登录也用，就放到这里了
import time  # 用于生成token
import random  # 用于生成token
from django.conf import settings  # 用于处理图片


# Create your views here.
# 学习重定向
def index(request):
    # return HttpResponseRedirect('/home')    #另一种方式
    return redirect('/home/')


def home(request):
    wheelsList = Wheel.objects.all()
    navList = Nav.objects.all()
    mustbyList = Mustbuy.objects.all()

    return render(request, 'axf/home.html',
                  {'title': '主页', 'wheelsList': wheelsList, 'navList': navList, 'mustbyList': mustbyList})


# 超市
def market(request, categoryid, cid, sortid):  # categoryid是产品总分类，cid是产品细分的分类
    leftSilder = Foodtypes.objects.all()
    if cid == '0':
        productList = Goods.objects.filter(categoryid=categoryid)  # 获取一类产品列表
    else:
        productList = Goods.objects.filter(categoryid=categoryid, childcid=cid)

    # 排序
    if sortid == '1':
        productList = productList.order_by('-productnum')
    elif sortid == '2':
        productList = productList.order_by('price')
    elif sortid == '3':
        productList = productList.order_by('-price')

    group = leftSilder.get(typeid=categoryid)  # 为了拿全部分类:0#牛奶:1这些数据
    childList = []  # 定义一个数组
    childnames = group.childtypenames
    # 开始切数据
    arr1 = childnames.split('#')
    for str in arr1:
        arr2 = str.split(':')
        obj = {'childName': arr2[0], 'childId': arr2[1]}
        childList.append(obj)

    return render(request, 'axf/market.html',
                  {'title': '超市', 'leftSilder': leftSilder, 'productList': productList, 'childList': childList,
                   'categoryid': categoryid, 'cid': cid})


# 购物车
def cart(request):
    return render(request, 'axf/cart.html', {'title': '购物车'})


def changecart(request, flag):
    # 判断是否登录
    token = request.session.get('token')
    if token == None:
        # 没登录
        return JsonResponse({'data':-1,'status':'error'})   #-1表示未登录
    else:
        productid=request.POST.get('productid')
        user=User.objects.get(userToken=token)
        if flag==0:
            pass
        elif flag==1:
            pass
        elif flag==2:
            pass
        elif flag==3:
            pass
        return JsonResponse({'data':1,'status':'success'})






def mime(request):
    username = request.session.get('username', '登录')
    # username=request.session['username']
    token = request.session.get('token')
    userImg = request.session.get('userImg')

    return render(request, 'axf/mime.html', {'title': '我的', 'username': username, 'token': token, 'userImg': userImg})


def base(request):
    wheelsList = Wheel.objects.all()
    return render(request, 'axf/base.html', {'wheelsList': wheelsList})


def default(request):
    wheelsList = Wheel.objects.all()
    return render(request, 'axf/default.html', {'wheelsList': wheelsList})


from .forms.login import LoginForm


def login(request):
    if request.method == 'POST':
        f = LoginForm(request.POST)
        if f.is_valid():  # 信息格式没问题的话
            nameid = f.cleaned_data['username']  # username
            pswd = f.cleaned_data['passwd']  # passwd
            print(nameid, pswd)

            try:
                user = User.objects.get(userAccount=nameid)
                if user.userPasswd != pswd:
                    return redirect('/login/')
            except User.DoesNotExist as e:
                return redirect('/login/')

            # 登录成功
            token = time.time() + random.randrange(1, 1000000)  # 时间加随机数
            user.userToken = str(token)
            user.save()  # 把token存进去
            request.session['username'] = user.userName  # 创建session，状态保持
            request.session['token'] = user.userToken  # token验证账户
            request.session['userImg'] = user.userImg
            return redirect('/mime/')

        else:  # 验证有问题
            return render(request, 'axf/login.html', {'title': '登录', 'form': f, 'error': f.errors})

    else:
        f = LoginForm()  # 如果不是POST把表单传进来
        return render(request, 'axf/login.html', {'title': '登录', 'form': f})


import time  # 用于生成token
import random  # 用于生成token
from django.conf import settings  # 用于处理图片
import os


def register(request):
    if request.method == 'POST':  # 如果是POST请求，要获取所有提交的值
        userAccount = request.POST.get('userAccount')
        userPasswd = request.POST.get('userPass')
        userName = request.POST.get('userName')
        userPhone = request.POST.get('userPhone')
        userAddress = request.POST.get('userAddress')
        userRank = 0
        token = time.time() + random.randrange(1, 1000000)  # 时间加随机数
        userToken = str(token)

        f = request.FILES['userImg']  # 拿到文件描述符
        imgStr = str(int(time.time())) + str(
            random.randrange(1000000, 19999999999)) + '.png'  # 网页绝对路径无法显示图片，只能分段生成，这里是图片的名字采用时间戳+随机数的方式生成，保证不会重名
        userImg = os.path.join(settings.MEDIA_ROOT, imgStr)  # 生成图片保存的路径
        imgStrSave = '/static/media/' + imgStr  # 这里是生成图片存储到数据库的名字

        # 保存图片
        with open(userImg, 'wb') as fp:
            for data in f.chunks():
                fp.write(data)
        user = User.createuser(userAccount, userPasswd, userName, userPhone, userAddress, imgStrSave, userRank,
                               userToken)
        user.save()  # 保存成功，重定向

        request.session['username'] = userName  # 创建session，状态保持
        request.session['token'] = userToken  # token验证账户
        request.session['userImg'] = imgStrSave

        return redirect('/mime/')

    else:
        return render(request, 'axf/register.html', {'title': '注册'})


from django.http import JsonResponse  # 如果取不到返回一段JSON数据，这里需要引用


# 验证离焦时是否账号已被注册
def checkuserid(request):
    userid = request.POST.get('userid')
    try:
        user = User.objects.get(userAccount=userid)  # 如果取到数据表示成功，不能再注册
        return JsonResponse({'data': '该用户已被注册', 'status': 'error'})  # 前面被data接收，后面被status接收
    except User.DoesNotExist as e:
        return JsonResponse({'data': '该用户可以注册', 'status': 'success'})  # 前面被data接收，后面被status接收,此时返回register的JS的AJAX里处理数据
    # 注意POST时如果403，就去settings.py中关闭csrf


# 退出登录
from django.contrib.auth import logout


def quit(request):
    logout(request)  # 清除了所有的session和cookies
    return redirect('/mime/')
