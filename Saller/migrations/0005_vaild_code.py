# Generated by Django 2.2.1 on 2019-10-08 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Saller', '0004_goods_goods_xiangqing'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vaild_Code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_content', models.CharField(max_length=8, verbose_name='验证码')),
                ('code_time', models.CharField(max_length=32, verbose_name='创建时间')),
                ('code_status', models.IntegerField(verbose_name='状态')),
                ('code_user', models.EmailField(max_length=254, verbose_name='邮箱')),
            ],
        ),
    ]
