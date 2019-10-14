# Generated by Django 2.2.1 on 2019-10-10 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Buyer', '0010_useraddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Buyer.LoginUserr'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='store_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Buyer.LoginUserr', verbose_name='店铺id'),
        ),
        migrations.AlterField(
            model_name='payorder',
            name='order_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Buyer.LoginUserr', verbose_name='订单用户'),
        ),
    ]
