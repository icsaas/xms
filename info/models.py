# -*- coding:utf-8 -*-
from django.db import models
import os
from datetime import date
from django.db import models
from django.db.models import permalink
import  Image
from django.db.models.fields.files import ImageFieldFile,FieldFile,FileField
from django.core.files.base import ContentFile
# Create your models here.
from django.utils.translation import  ugettext_lazy
import tempfile
import StringIO
class NewImageFieldFile(ImageFieldFile):
    def save(self,name,content,save=True):
        temp_file=tempfile.TemporaryFile()
        f=StringIO.StringIO(content.read())
        image=Image.open(f)
        #get the max size of the image
        max_width,max_height=self.field.max_width,self.field.max_height
        #process pic
        image.save(temp_file,'JPEG')
        temp_file.seek(0)
        content2=ContentFile(temp_file.read())
        content.close()
        temp_file.close()
        super(NewImageFieldFile,self).save(name,content2,save)

class NewImageField(models.ImageField):
    attr_class = NewImageFieldFile
    def __init__(self,verbose_name=None,name=None,width_field=None,height_field=None,thumbnail_path=None,max_size=(600,600),**kwargs):
        self.width_field,self.height_field=width_field,height_field
        self.thumbnail_path=thumbnail_path
        self.max_width,self.max_height=max_size[0],max_size[1]
        #self.verbose_name=verbose_name
        #super(NewImageFieldFile,self).__init__(self.verbose_name,name,**kwargs)
        models.ImageField.__init__(self,verbose_name,name,**kwargs)


class Cquenv(models.Model):
    pass

class MyThing(models.Model):
    name=models.CharField(max_length=100,help_text=ugettext_lazy('This is the help text'))

class Category(models.Model):
    title=models.CharField(max_length=100,db_index=True,verbose_name="名字")
    slug=models.SlugField(max_length=100,db_index=True,verbose_name="缩写")
    def __unicode__(self):
        return self.title
    class Meta:
        ordering=('title',)
        verbose_name_plural="类别"
        verbose_name="类别"

class Info(models.Model):
    title=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100,unique=True)
    body=models.TextField()
    posted=models.DateTimeField(db_index=True,auto_now_add=True)
    category=models.ForeignKey(Category)
    def __unicode__(self):
        return '%s' %self.title
    class Meta:
        ordering=('posted',)
class Leaders(models.Model):
    name=models.CharField(max_length=100,verbose_name="姓名")
    position=models.CharField(max_length=100,verbose_name="职位")
    direction=models.CharField(max_length=100,verbose_name="研究方向")
    office=models.CharField(max_length=100,verbose_name="办公室")
    telnumber=models.CharField(max_length=100,verbose_name="电话")
    email=models.EmailField(verbose_name="电子邮件")
    exprience=models.TextField(verbose_name="工作经历")
    otherpositon=models.TextField(verbose_name="兼职")
    honor=models.TextField(verbose_name="荣誉")
    money=models.TextField(verbose_name="科研项目及经费")
    domain=models.TextField(verbose_name="研究领域")
    thesis=models.TextField(verbose_name="论文及专利")
    conference=models.TextField(verbose_name="会议")
    photo=models.ImageField(upload_to='images/teachers',verbose_name="照片",null=True)
    category=models.ForeignKey(Category,verbose_name="分类")
    def __unicode__(self):
        return '%s' %self.name

    class Meta:
        ordering=('name',)
        verbose_name_plural="课题组领导信息"
        verbose_name="课题组领导信息"
    def save(self, force_insert=False, force_update=False, using=None):
        filename=self.photo.path
        img=Image.open(filename)
        #processing photo

        super(Leaders,self).save(force_insert,force_update)

class Members(models.Model):
    degree=models.CharField(max_length=100,verbose_name="学位")
    detail=models.TextField(verbose_name="具体成员")
    category=models.ForeignKey(Category,verbose_name="类别")
    photo=models.ImageField(upload_to='images/members',verbose_name="照片",null=True)
    def __unicode__(self):
        return '%s' %self.degree
    class Meta:
        ordering=('degree',)
        verbose_name="课题组其他成员"
        verbose_name_plural="课题组其他成员"



class Graduate(models.Model):
    name=models.CharField(max_length=100,blank=True,verbose_name="姓名")
    job=models.CharField(max_length=100,blank=True,verbose_name="工作单位")
    position=models.CharField(max_length=100,verbose_name="职位")
    address=models.CharField(max_length=200,verbose_name="地址")
    telnumber=models.CharField(max_length=100,verbose_name="电话")
    qqnumber=models.CharField(max_length=100,verbose_name="QQ")
    email=models.EmailField(verbose_name="电子邮件")
    photo=NewImageField(upload_to='images/graduates',null=True,verbose_name="图片")
    category=models.ForeignKey(Category,verbose_name="类别")
    def __unicode__(self):
        return '%s' %self.name
    class Meta:
        ordering=('name',)
        verbose_name_plural="毕业生"
        verbose_name="毕业生"

class Device(models.Model):
    name=models.CharField(max_length=100,verbose_name="设备名字")
    detail=models.TextField(verbose_name="详细介绍")
    photo=models.ImageField(upload_to='images/devices',verbose_name="图片")
    category=models.ForeignKey(Category,verbose_name="类别")

    def __unicode__(self):
        return '%s' %self.name
    class Meta:
        ordering=('name',)
        verbose_name="实验设备"
        verbose_name_plural="实验室设备"

class LibNotice(models.Model):
    name=models.CharField(max_length=100,verbose_name="实验室手册名称")
    detail=models.TextField(verbose_name="详细内容")
    category=models.ForeignKey(Category,verbose_name="类别")

    def __unicode__(self):
        return '%s' %self.name
    class Meta:
        ordering=('name',)
        verbose_name="实验室手册"
        verbose_name_plural="实验室手册"

class ResearchDirection(models.Model):
    name=models.CharField(max_length=150,verbose_name="研究方向名称")
    slug=models.SlugField(max_length=100,unique=True,verbose_name="英文简写")
    members=models.CharField(max_length=150,verbose_name="组内成员")
    detail=models.TextField(verbose_name="详细内容")
    features=models.TextField(verbose_name="优势与特色")
    category=models.ForeignKey(Category,verbose_name="类别")

    def __unicode__(self):
        return '%s' %self.name
    class Meta:
        ordering=('name',)
        verbose_name="研究方向"
        verbose_name_plural="研究方向"

class Contact(models.Model):
    SEX_CHOICES=(
        (u'男',u'男'),
        (u'女',u'女'),
    )
    name=models.CharField(max_length=40,verbose_name="姓名")
    sex=models.CharField(max_length=2,choices=SEX_CHOICES,verbose_name="性别")
    phone=models.CharField(max_length=30,blank=True,null=True,verbose_name="电话")
    qq=models.CharField(max_length=30,blank=True,null=True,verbose_name="qq")
    birth=models.DateField(blank=True,null=True,verbose_name="生日")

    def __unicode__(self):
        return u'%s %s' %(self.name,self.phone)
    class  Meta:
        ordering=['name']
        verbose_name="通讯录"
        verbose_name_plural="通讯录"







