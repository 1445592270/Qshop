
from django.urls import path,re_path
from Buyer.views import *

urlpatterns = [
path('indexx/',indexx),
path('loginn/',loginn),
path('registerr/',registerr),
path('logout/',logout),
path('goods_list/',goods_list),
path('user_center_info/',user_center_info),
path('place_order/',place_order),
path('cart/',cart),
path('user_center_order/',user_center_order),
path('user_center_site/',user_center_site),
path('AlipayViews/',AlipayViews),
path('payresult/',payresult),
re_path('detail/(?P<id>\d+)',detail),

]