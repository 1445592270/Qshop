
from django.urls import path,re_path
from Buyer.views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
path('indexx/',indexx),
path('loginn/',loginn),
path('registerr/',registerr),
path('logout/',logout),
# path('goods_list/',goods_list),
# path('goods_list/',cache_page(60*15)(goods_list)),   #设置缓存
path('goods_list/',goods_list),
path('user_center_info/',user_center_info),
path('place_order/',place_order),
path('cart/',cart),
path('user_center_order/',user_center_order),
path('user_center_site/',user_center_site),
path('AlipayViews/',AlipayViews),
path('payresult/',payresult),
path('add_cart/',add_cart),
path('place_order_more/',place_order_more),
path('reqtest/',reqtest),
path('myprocess_tem_rep/',myprocess_tem_rep),
re_path('detail/(?P<id>\d+)',detail),

]