
from django.urls import path,re_path
from Saller.views import *

urlpatterns = [
    path('register/',register),
    path('login/',login),
    # path('login1/',login1),
    path('index/',index),
    path('logout/',logout),
    path('goods_list/',goods_list),
    re_path('goods_list/(?P<status>[01])/(?P<page>\d+)',goods_list),
    re_path('goods_status/(?P<status>\w+)/(?P<id>\d+)',goods_status),
    path('personal_info/',personal_info),
    path('goods_add/',goods_add),
    path('get_code/',get_code),
    path('sendemail/',sendemail),
    path('seller_caozuo/',seller_caozuo),
    # path('order/',order),
    re_path('order/(?P<status>\d{1})',order),
]