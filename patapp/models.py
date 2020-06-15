from django.db import models
import django.utils.timezone as timezone

# Create your models here.


class doctor(models.Model):
    doctor_id=models.CharField(primary_key=True,max_length=64,default='',unique=True)

    class Meta:
        verbose_name = u"医生信息"
        verbose_name_plural = verbose_name

class user(models.Model):
    openid = models.CharField('openId', primary_key=True, max_length=64, null=False, default='', unique=True)
    session_key = models.CharField(verbose_name='session_key', max_length=256)
    gender = models.CharField('性别', max_length=64, null=False, default='请填写性别')
    name = models.CharField('语言', max_length=64, null=False, default='')
    mobile = models.CharField(verbose_name='小程序授权手机号', max_length=32, default='请填写手机号')
    age = models.CharField('年龄', max_length=64, null=False, default='请填写年龄')
    avatarimg = models.ImageField(upload_to='images', max_length=512, null=False, default='')
    first_date= models.DateField(default = '2020-05-04')
    doctor= models.ForeignKey('doctor',on_delete=models.CASCADE,default='1')
    class Meta:
        verbose_name=u"患者信息"
        verbose_name_plural=verbose_name

class image(models.Model):
    upload_key = models.CharField(primary_key=True, max_length=64, null=False, default='', unique=True)
    upload_time = models.CharField(max_length=64, null=False, default='')
    text = models.TextField(default='[]', db_index=True)
    reply = models.TextField(default='[]')
    user = models.ForeignKey('user',on_delete=models.CASCADE)

    class Meta:
        verbose_name=u"患者提交信息"
        verbose_name_plural=verbose_name

class imagereal(models.Model):
    img = models.ImageField('伤口图像', upload_to='images', max_length=512, null=False, default='')
    imglocal = models.ImageField('伤口图像', upload_to='images', max_length=512, null=False, default='')
    image = models.ForeignKey('image', on_delete=models.CASCADE)
    class Meta:
        verbose_name=u"患者上传图像"
        verbose_name_plural=verbose_name