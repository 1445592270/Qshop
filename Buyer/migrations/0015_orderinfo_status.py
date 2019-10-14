# Generated by Django 2.2.1 on 2019-10-11 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buyer', '0014_auto_20191011_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderinfo',
            name='status',
            field=models.IntegerField(choices=[(0, '未支付'), (1, '已支付'), (2, '已发货'), (3, '已完成'), (4, '拒绝订单')], default=0, verbose_name='订单详情状态'),
        ),
    ]
