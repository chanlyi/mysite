# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SightInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='姓名', max_length=45)),
                ('gender', models.IntegerField(verbose_name='性别', default=-1)),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('address', models.CharField(verbose_name='地址', max_length=255)),
                ('phone', models.CharField(verbose_name='电话', max_length=45)),
                ('needpost', models.IntegerField(choices=[(-1, '未选择'), (0, '不邮寄'), (1, '邮寄')], verbose_name='是否邮寄')),
                ('diopter', models.CharField(verbose_name='屈光度', max_length=45)),
                ('corrected_sight', models.FloatField(verbose_name='矫正视力', max_length=11)),
                ('glass_frame_type', models.CharField(verbose_name='镜架型号', max_length=45)),
                ('glass_lens_type', models.CharField(verbose_name='镜片型号', max_length=45)),
                ('eye_mid_distance', models.CharField(verbose_name='瞳距', max_length=45)),
                ('optometist', models.CharField(verbose_name='眼光师', max_length=45)),
                ('comment', models.CharField(verbose_name='备注', max_length=45)),
                ('newdate', models.DateField(verbose_name='日期')),
                ('uptime', models.DateTimeField(verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '眼视光记录表',
                'verbose_name_plural': '眼视光记录表',
            },
        ),
    ]
