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
from django.views.decorators.cache import cache_page
import logging
collect=logging.getLogger('django')
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
        print(email)
        if email and session_email and email == session_email:
            user_email=LoginUserr.objects.filter(email=email).exists()
            print(user_email)
            if user_email:
                return func(request,*args,**kwargs)
            else:
                return HttpResponseRedirect('/Buyer/loginn/')
        else:
            return HttpResponseRedirect('/Buyer/loginn/')
    return inner
# @cache_page(60*20)
@LoginVaild
def indexx(request):
    # print('im view')
    # 1/0
    goods_type=GoodsType.objects.all()
    result=[]
    for type in goods_type:
        goods=type.goods_set.order_by('-goods_price')
        if len(goods)>4:
            goods=goods[:4]
            result.append({'type':type,'goods':goods})
            collect.warning('---------%s is login----')
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
                    # collect.info('---------%s is login----'%user.email)
                    collect.warning('---------%s is login----'%user.email)
                    return response
                else:
                    error_msg = "密码错误"
            else:
                error_msg = "用户不存在"
        else:
            error_msg = "邮箱不可以为空"
    return render(request,'buyer/login.html',locals())
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

    request.session.flush()
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


#购物车
def cart(request):
    user_id=request.COOKIES.get('userid')
    cart_list=[]
    cart=Cart.objects.filter(user_id=user_id).order_by('-id')
    count = cart.count()  # 获取条数
    for i in cart:
        if i.order_number!='0':
            payorder=PayOrder.objects.get(order_number=i.order_number)
            if payorder.order_status!=1:
                cart_list.append(i)
            else:
                count-=1
        else:
            cart_list.append(i)

    return render(request,'buyer/cart.html',locals())

@LoginVaild
def user_center_site(request):
    result={'code':100000,'content':''}
    address=UserAddress.objects.all()
    user_email=request.COOKIES.get('email')
    if request.method=='POST':
        loginuser=LoginUserr.objects.filter(email=user_email).first()
        if loginuser:
            useraddress=UserAddress()
            useraddress.user_name=request.POST.get('user_name')
            useraddress.user_address=request.POST.get('user_address')
            useraddress.user_post=request.POST.get('user_post')
            useraddress.user_phone=request.POST.get('user_phone')
            useraddress.user_id=loginuser.id
            useraddress.save()
        else:
            result['code']=100001
            result['content']='用户不存在'
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
    ## 修改订单详情的状态
    ## 查询订单详情
    order_info = paryorder.orderinfo_set.all()
    for one in order_info:
        one.status = 1
        one.save()
    paryorder.save()
    return render(request,'buyer/payresult.html',locals())


@LoginVaild
def add_cart(request):
    result={'code':100000,'content':''}
    if request.method=='POST':
        goods_id=request.POST.get('goods_id')
        count=int(request.POST.get('count',1))
        user_id=request.COOKIES.get('userid')
        goods=Goods.objects.get(id=goods_id)
        cart=Cart()
        cart.goods_number=count
        cart.goods_price=goods.goods_price
        cart.goods_total=goods.goods_price*count
        cart.goods=goods
        cart.user=LoginUserr.objects.get(id=user_id)
        cart.save()
        result['code']=100001
        result['content']='商品添加成功'
    else:
        result['code'] = 100002
        result['content'] = '请求方式不正确'
    return JsonResponse(result)

@LoginVaild
def place_order(request):
    ## 保存订单
    goods_id = request.GET.get("goods_id")  # 商品id
    print('goods_id',goods_id)
    goods_count = request.GET.get("goods_count")  ## 订单数量
    print('goods_count',goods_count)
    user_id = request.COOKIES.get("userid")
    if goods_id and goods_count:
        goods_id = int(goods_id)
        goods_count = int(goods_count)
        goods = Goods.objects.get(id=goods_id)
        print(goods.goods_price)
        ## 保存订单表
        payorder = PayOrder()
        order_number = str(time.time()).replace('.', '')  ## 生产订单编号
        payorder.order_number = order_number  ## 订单编号
        payorder.order_status = 0
        payorder.order_total = goods.goods_price * goods_count
        print(payorder.order_total)
        payorder.order_user = LoginUserr.objects.get(id=user_id)
        payorder.save()
        ## 保存订单详情表
        orderinfo = OrderInfo()
        orderinfo.order_id = payorder
        print('orderinfo.order_id',orderinfo.order_id)
        orderinfo.goods = goods
        orderinfo.goods_count = goods_count
        orderinfo.goods_price = goods.goods_price
        orderinfo.goods_total_price = goods.goods_price * goods_count
        print('orderinfo.goods_total_price',orderinfo.goods_total_price)
        orderinfo.store_id = goods.goods_store
        orderinfo.save()

        total_count=0
        all_goods_info=payorder.orderinfo_set.all()
        for i in all_goods_info:
            total_count+=i.goods_count
    return render(request,'buyer/place_order.html',locals())

@LoginVaild
def place_order_more(request):
    """
        获取不到id相同的商品
        goods_1=on
        &goods_3=on
        &goods_2=on
        &goods_3=on
        &goods_2=on
        &count_1=1
        &count_3=1
        &count_3=1
        &count_2=5
        &count_2=1
        """
    data=request.GET
    # for i in data:
    #     print(i)

    userid=request.COOKIES.get('userid')
    print('userid',userid)
    data_item=data.items()
    # print(data_item)
    req_data=[]
    for key,val in data_item:
        if key.startswith('goods'):
            # print('key****',key,'val****',val)
            # print('all*******',key.startswith('count_'))
            goods_id=key.split('_')[1]
            count=data.get('count_'+goods_id)
            # print('count',count)
            cart_id=key.split('_')[2]
            # print('%s++++++%s'%(goods_id,count))
            req_data.append((int(goods_id),int(count),int(cart_id)))
    # print('req_data',req_data)
    if req_data:
        payorder = PayOrder()
        order_number = str(time.time()).replace('.', '')  ## 生产订单编号
        payorder.order_number = order_number  ## 订单编号
        payorder.order_status = 0
        payorder.order_total = 0
        payorder.order_user=LoginUserr.objects.get(id=userid)
        payorder.save()
        order_total=0
        total_count=0

        #订单详情保存  i为商品id  j为数量 k为购物车id
        for i,j,k in req_data:
            goods=Goods.objects.get(id=i)
            orderinfo = OrderInfo()
            orderinfo.order_id = payorder
            orderinfo.goods = goods
            orderinfo.goods_count = j
            orderinfo.goods_price=goods.goods_price
            orderinfo.goods_total_price = goods.goods_price * j
            orderinfo.store_id = goods.goods_store
            orderinfo.save()
            order_total+=goods.goods_price * j
            total_count+=j

            cart=Cart.objects.get(id=k)
            cart.order_number=order_number
            cart.save()
        payorder.order_total=order_total
        payorder.save()

    return render(request,'buyer/place_order.html',locals())

#订单
@LoginVaild
def user_center_order(request):
    user_id=request.COOKIES.get('userid')
    user=LoginUserr.objects.get(id=int(user_id))
    payorder=user.payorder_set.order_by('order_status')

    return render(request,'buyer/user_center_order.html',locals())





from CeleryTask.tasks import *
def reqtest(request):
    test.delay()
    return HttpResponse('celery test ')


def myprocess_tem_rep(request):
    def test():
        return HttpResponse('my test')
    rep=HttpResponse('myprocess_tem_rep')
    rep.render=test
    return rep


