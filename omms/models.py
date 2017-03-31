"""
眼光配镜记录

日期，姓名，性别，年龄，地址，电话，是否邮寄，
屈光度，矫正视力，镜架型号，镜片型号，瞳距，眼光师，备注
"""
from django.db import models

GENDER = (
    ("未知", "未知"),
    ("女", "女"),
    ("男", "男"),
    ("儿童", "儿童"),
)

NEEDPOST = (
    (-1, "未选择"),
    (0, "不邮寄"),
    (1, "邮寄"),
)


# Create your models here.
class SightInfo(models.Model):
    name = models.CharField(max_length=45, blank=False, null=False, verbose_name="姓名")
    gender = models.CharField(max_length=45, verbose_name="性别")
    age = models.IntegerField(verbose_name="年龄")
    address = models.CharField(max_length=255, verbose_name="地址")
    phone = models.CharField(max_length=45, verbose_name="电话")
    needpost = models.IntegerField(choices=NEEDPOST, verbose_name="是否邮寄")
    diopter = models.CharField(max_length=45, verbose_name="屈光度")
    corrected_sight = models.CharField(max_length=45, verbose_name="矫正视力")
    glass_frame_type = models.CharField(max_length=45, verbose_name="镜架型号")
    glass_lens_type = models.CharField(max_length=45, verbose_name="镜片型号")
    eye_mid_distance = models.CharField(max_length=45, verbose_name="瞳距")
    optometist = models.CharField(max_length=45, verbose_name="验光师")
    comment = models.CharField(max_length=45, verbose_name="备注")
    newdate = models.DateField(verbose_name="日期")
    uptime = models.DateTimeField(verbose_name="更新时间")

    class Meta:
        managed = False
        verbose_name = u"眼视光记录表"
        verbose_name_plural = u"眼视光记录表"
        app_label = 'omms'
