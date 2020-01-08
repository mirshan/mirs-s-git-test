from django.db import models

# Create your models here.
class Wheel(models.Model):
    img=models.CharField(max_length=150)
    name=models.CharField(max_length=20)
    trackid=models.CharField(max_length=20)
    isDelete=models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = '轮播大图'

class Nav(models.Model):
    img=models.CharField(max_length=150)
    name=models.CharField(max_length=20)
    trackid=models.CharField(max_length=20)
    isDelete=models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = '类别导航'

class Mustbuy(models.Model):
    img=models.CharField(max_length=150)
    name=models.CharField(max_length=20)
    trackid=models.CharField(max_length=20)
    isDelete=models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = '必买小轮播'

class Foodtypes(models.Model):
    typeid=models.IntegerField()
    typename=models.CharField(max_length=50)
    childtypenames=models.CharField(max_length=50)
    typesort=models.IntegerField()
    idDelete=models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = '商品类别'

class Goods(models.Model):
    productid=models.IntegerField()
    productimg=models.CharField(max_length=100)
    productname=models.CharField(max_length=100)
    productlongname=models.CharField(max_length=200)
    isxf=models.BooleanField(default=0)
    pmdesc=models.IntegerField()
    specifics=models.CharField(max_length=50)
    price=models.IntegerField()
    marketprice=models.IntegerField()
    categoryid=models.IntegerField()
    childcid=models.IntegerField()
    childcidname=models.CharField(max_length=50)
    dealerid=models.IntegerField()
    storenums=models.IntegerField()
    productnum=models.IntegerField()
    class Meta:
        verbose_name_plural = '商品表'

#用户模型类
class User(models.Model):
    userAccount=models.CharField(max_length=20,unique=True,verbose_name='账号')
    userPasswd=models.CharField(max_length=20,verbose_name='密码')
    userName=models.CharField(max_length=20,verbose_name='昵称')
    userPhone=models.CharField(max_length=20,verbose_name='手机')
    userAddress=models.CharField(max_length=100,verbose_name='地址')
    userImg=models.CharField(max_length=150,verbose_name='图片')
    userRank=models.IntegerField(verbose_name='等级')        #用户等级
    #token验证值，每次登录之后都会更新，一定要有
    userToken=models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = '用户列表'

    @classmethod    #创建用户
    def createuser(cls,account,passwd,name,phone,address,img,rank,token):
        u=cls(userAccount=account,userPasswd=passwd,userName=name,userPhone=phone,userAddress=address,userImg=img,userRank=rank,userToken=token)
        return u

