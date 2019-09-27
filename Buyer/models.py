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
    order_status = models.IntegerField(verbose_name="订单状态")
    order_total = models.FloatField(verbose_name="订单总价 ")
    order_user = models.ForeignKey(to= LoginUser,on_delete=models.CASCADE,verbose_name="订单用户")## 外键  链接到  用户表


## 订单详情表
class OrderInfo(models.Model):
    order_id = models.ForeignKey(to=PayOrder,on_delete=models.CASCADE,verbose_name="订单表外键")
    goods = models.ForeignKey(to=Goods,on_delete=models.CASCADE,verbose_name="商品表")
    goods_count = models.IntegerField(verbose_name="商品数量")
    goods_total_price = models.FloatField(verbose_name="商品小计")
    store_id = models.ForeignKey(to=LoginUser,on_delete=models.CASCADE,verbose_name="店铺id")