from django.db import models
from Saller.models import *
# Create your models here.
class LoginUserr(models.Model):
    ## id 不需要写
    email = models.EmailField()
    password = models.CharField(max_length=32)
    username = models.CharField(max_length=32,null=True,blank=True)
    phone_number = models.CharField(max_length=11,null=True,blank=True)
    photo = models.ImageField(upload_to="images",null=True,blank=True)   ## /static/images
    age = models.IntegerField(null=True,blank=True)
    gender = models.CharField(null=True,blank=True,max_length=4)
    address = models.TextField(null=True,blank=True)


ORDER_STATUS=(
    (0,'未支付'),
    (1,'已支付'),
    (2,'待发货'),
    (3,'待收货'),
    (4,'完成'),
    (5,'拒收'),
)

## 订单表
class PayOrder(models.Model):
    ###订单状态：
    # 0 未支付
    # 1 已支付
    # 2  待发货
    # 3  待收货
    # 4   完成
    # 5   拒收
    order_number = models.CharField(max_length=32,verbose_name="订单编号",unique=True)
    order_date = models.DateField(auto_now=True,verbose_name="订单日期")
    # order_status = models.IntegerField(verbose_name="订单状态")
    order_status=models.IntegerField(choices=ORDER_STATUS,verbose_name='订单状态')
    order_total = models.FloatField(verbose_name="订单总价 ")
    order_user = models.ForeignKey(to= LoginUserr,on_delete=models.CASCADE,verbose_name="订单用户")## 外键  链接到  用户表


ORDERINFO_STATUS=(
    (0,'未支付'),
    (1,'已支付'),
    (2,'已发货'),
    (3,'已完成'),
    (4,'拒绝订单'),
)
## 订单详情表
class OrderInfo(models.Model):
    order_id = models.ForeignKey(to=PayOrder,on_delete=models.CASCADE,verbose_name="订单表外键")
    goods = models.ForeignKey(to=Goods,on_delete=models.CASCADE,verbose_name="商品表")
    goods_price = models.FloatField(verbose_name='商品单价')
    goods_count = models.IntegerField(verbose_name="商品数量")
    goods_total_price = models.FloatField(verbose_name="商品小计")
    store_id = models.ForeignKey(to=LoginUser,on_delete=models.CASCADE,verbose_name="店铺id")
    status = models.IntegerField(choices=ORDERINFO_STATUS,verbose_name='订单详情状态',default=0)

class Cart(models.Model):
    goods_number=models.IntegerField(verbose_name='商品数量')
    goods_price=models.FloatField(verbose_name='商品价格')
    goods_total=models.FloatField(verbose_name='商品总价')
    goods=models.ForeignKey(to=Goods,on_delete=models.CASCADE)
    user=models.ForeignKey(to=LoginUserr,on_delete=models.CASCADE)
    order_number=models.CharField(max_length=32,default=0)


class UserAddress(models.Model):
    user_name=models.CharField(max_length=10)
    user_address=models.CharField(max_length=50)
    user_post=models.CharField(max_length=32)
    user_phone=models.CharField(max_length=22)
    status=models.IntegerField(default=0)
    user=models.ForeignKey(to=LoginUserr,on_delete=models.CASCADE)