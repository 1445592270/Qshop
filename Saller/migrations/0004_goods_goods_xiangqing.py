# Generated by Django 2.2.1 on 2019-09-25 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Saller', '0003_goodstype_type_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='goods_xiangqing',
            field=models.TextField(default='好看吗，好看就好吃！！！'),
        ),
    ]