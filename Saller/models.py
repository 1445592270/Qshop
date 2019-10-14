from django.db import models
from django.db.models import Manager

# Create your models here.
class LoginUser(models.Model):
    ## id 不需要写
    email = models.EmailField()
    password = models.CharField(max_length=32)
    username = models.CharField(max_length=32,null=True,blank=True)
    phone_number = models.CharField(max_length=11,null=True,blank=True)
    photo = models.ImageField(upload_to="images",null=True,blank=True)   ## /static/images
    age = models.IntegerField(null=True,blank=True)
    gender = models.CharField(null=True,blank=True,max_length=4)
    address = models.TextField(null=True,blank=True)

    ###  null 针对数据库，表示可以为空，即在数据库的存储中可以为空
    ### blank 针对表单，表示在表单中该字段可以不填，但是对数据库没有影响

class MyGoodsType(Manager):
    def myaddtype(self,type_label,type_description,type_picture='images/banner01.jpg'):
        goods_type=GoodsType()
        goods_type.type_label=type_label
        goods_type.type_description=type_description
        goods_type.type_picture=type_picture
        goods_type.save()
        return goods_type



class GoodsType(models.Model):
    type_label=models.CharField(max_length=32)
    type_description=models.TextField()
    type_picture = models.ImageField(upload_to="images")
    objects=MyGoodsType()
class Goods(models.Model):
    goods_number = models.CharField(max_length=11)
    goods_name = models.CharField(max_length=32)
    goods_price = models.FloatField()
    goods_count = models.IntegerField()
    goods_location = models.CharField(max_length=254,verbose_name="产地")
    goods_safe_date = models.IntegerField()
    goods_status = models.IntegerField()  ## 0 代表下架  1 代表在售
    goods_pro_time = models.DateField(auto_now=True,verbose_name="生产日期")
    picture=models.ImageField(upload_to='images')
    goods_xiangqing=models.TextField(default='好看吗，好看就好吃！！！')

    goods_type=models.ForeignKey(to=GoodsType,on_delete=models.CASCADE,default=1)
    goods_store=models.ForeignKey(to=LoginUser,on_delete=models.CASCADE,default=1)

class MyGoodsFilter(Manager):
    def myfilter(self):
        data=Goods.objects.filter(id__lt=10).values('goods_name')
        return data



class Vaild_Code(models.Model):
    code_content = models.CharField(max_length=8,verbose_name="验证码")
    code_time = models.CharField(max_length=32,verbose_name="创建时间")
    code_status = models.IntegerField(verbose_name="状态")    ##1 使用  0 未使用
    code_user = models.EmailField(verbose_name="邮箱")



# class UserAddress(models.Model):
#     user_name=models.CharField(max_length=10)
#     user_address=models.CharField(max_length=50)
#     user_post=models.CharField(max_length=32)
#     user_phone=models.CharField(max_length=22)
#     status=models.IntegerField(default=0)
#     user=models.ForeignKey(to=LoginUser,on_delete=models.CASCADE)



