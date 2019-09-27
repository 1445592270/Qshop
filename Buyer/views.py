from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse

from Saller.models import *
from Buyer.models import *

import hashlib
from django.core.paginator import Paginator
import time
from alipay import AliPay
from Qshop.settings import alipay_public_key_string,alipay_private_key_string
# Create your views here.


## 密码加密
def setPassword(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    result = md5.hexdigest()
    return result
def LoginVaild(func):
    ## 1. 获取cookie中username和email
    ## 2. 判断username和email
    ## 3. 如果成功  跳转
    ## 4. 如果失败   login.html
    def inner(request,*args,**kwargs):
        email = request.COOKIES.get('email')
        ## 获取session
        session_email = request.session.get("email")
        if email and session_email and email == session_email:
            return func(request,*args,**kwargs)
        else:
            return HttpResponseRedirect('/Buyer/loginn/')
    return inner

def indexx(request):
    goods_type=GoodsType.objects.all()
    result=[]
    for type in goods_type:
        goods=type.goods_set.order_by('-goods_price')
        if len(goods)>4:
            goods=goods[:4]
            result.append({'type':type,'goods':goods})
    return render(request,'buyer/index.html',locals())
def loginn(request):
    if request.method == "POST":
        error_msg = ""
        email = request.POST.get("email")
        password = request.POST.get("password")
        if email:
            user = LoginUserr.objects.filter(email=email).first()
            print(user.email)
            if user:
                ## 存在
                if user.password == setPassword(password):
                    ## 登录成功
                    ## 跳转页面
                    # error_msg = "登录成功"
                    # return HttpResponseRedirect('/index/')
                    ## 设置cookie
                    response  = HttpResponseRedirect("/Buyer/indexx/")
                    response.set_cookie("email",user.email)
                    response.set_cookie("userid",user.id)
                    request.session['email'] = user.email  ## 设置session
                    return response
                else:
                    error_msg = "密码错误"
            else:
                error_msg = "用户不存在"
        else:
            error_msg = "邮箱不可以为空"
    return render(request,'buyer/login.html')
def registerr(request):
    if request.method=='POST':
        error=''
        email=request.POST.get('email')
        password=request.POST.get('password')
        password2=request.POST.get('password2')
        if email and password and password2:
            loginuserr=LoginUserr.objects.filter(email=email).first()
            if not loginuserr:
                if password==password2:
                    user=LoginUserr()
                    user.email=email
                    # user.username=email
                    user.password=setPassword(password)
                    user.save()
                    error='注册成功'
                else:
                    error='两次密码不一致'
            else:
                error='邮箱已存在，请登录'
        else:
            error='用户名或密码不能为空'
    return render(request,'buyer/register.html',locals())
## 登出
def logout(request):
    # 删除cookie   删除  session
    response = HttpResponseRedirect("/Buyer/loginn/")
    # response.delete_cookie("kename")
    keys = request.COOKIES.keys()
    for one in keys:
        response.delete_cookie(one)

    del request.session['email']
    return response


def goods_list(request):
    # goods=Goods.objects.all()
    # recommend=Goods.objects.order_by("-goods_pro_time")
    # """
    # 根据 keywords传递的类型id，寻找该类型下面的商品
    # """
    keywords = request.GET.get("keywords")
    req_type=request.GET.get('req_type')
    if req_type=='findall':
        goods_type = GoodsType.objects.get(id=keywords)
        goods = goods_type.goods_set.all()   ## 反向查询，
    elif req_type=='search':
        goods=Goods.objects.filter(goods_name__contains=keywords).all()
    end = len(goods) // 5
    end += 1
    recommend = goods.order_by("-goods_pro_time")[:end]
    return render(request,"buyer/goods_list.html",locals())

#详情
def detail(request,id):
    goods=Goods.objects.get(id=int(id))
    return render(request,'buyer/detail.html',locals())
#用户中心
def user_center_info(request):
    return render(request,'buyer/user_center_info.html',locals())
@LoginVaild
def place_order(request):
    ## 保存订单
    goods_id = request.GET.get("goods_id")  # 商品id
    goods_count = request.GET.get("goods_count")  ## 订单数量
    user_id = request.COOKIES.get("userid")
    if goods_id and goods_count:
        goods_id = int(goods_id)
        goods_count = int(goods_count)
        goods = Goods.objects.get(id=goods_id)
        ## 保存订单表
        payorder = PayOrder()
        order_number = str(time.time()).replace('.', '')  ## 生产订单编号
        payorder.order_number = order_number  ## 订单编号
        payorder.order_status = 0
        payorder.order_total = goods.goods_price * goods_count
        payorder.order_user = LoginUser.objects.get(id=user_id)
        payorder.save()
        ## 保存订单详情表
        orderinfo = OrderInfo()
        orderinfo.order_id = payorder
        orderinfo.goods = goods
        orderinfo.goods_count = goods_count
        orderinfo.goods_total_price = goods.goods_price * goods_count
        orderinfo.store_id = goods.goods_store
        orderinfo.save()

        total_count=0
        all_goods_info=payorder.orderinfo_set.all()
        for i in all_goods_info:
            total_count+=i.goods_count
    return render(request,'buyer/place_order.html',locals())

#购物车
def cart(request):
    return render(request,'buyer/cart.html',locals())
#订单
def user_center_order(request):
    return render(request,'buyer/user_center_order.html',locals())

def user_center_site(request):
    return render(request,'buyer/user_center_site.html',locals())

def AlipayViews(request):
    payorder_id=request.GET.get('payorder_id')
    payorder=PayOrder.objects.get(id=payorder_id)
    ## 实例化支付对象
    alipay = AliPay(
        appid='2016101300674021',
        app_notify_url=None,
        app_private_key_string=alipay_private_key_string,
        alipay_public_key_string=alipay_public_key_string,
        sign_type="RSA2",
    )
    ## 实例化订单
    order_string = alipay.api_alipay_trade_page_pay(
        subject='牛羊生鲜',  ## 交易主题
        out_trade_no=payorder.order_number,  ## 订单号
        total_amount=payorder.order_total,  ## 交易总金额
        return_url='http://127.0.0.1:8000/Buyer/payresult',  ##  请求支付，之后及时回调的一个接口
        notify_url='http://127.0.0.1:8000/Buyer/payresult'  ##  通知地址，
    )
    ##   发送支付请求
    ## 请求地址  支付网关 + 实例化订单
    result = "https://openapi.alipaydev.com/gateway.do?" + order_string
    print(result)
    return HttpResponseRedirect(result)

def payresult(request):
    data=request.GET
    order_number=request.GET.get('out_trade_no')
    paryorder=PayOrder.objects.get(order_number=order_number)
    paryorder.order_status=1
    paryorder.save()
    return render(request,'buyer/payresult.html',locals())