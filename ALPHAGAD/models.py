from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import IntegerRangeField

# Create your models here.
class alpha_signup(AbstractUser):
    firstname=models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    pincode=models.IntegerField(null=True)
    email = models.EmailField(max_length=30)
    phonenumber=models.IntegerField(null=True)
    astatus=models.IntegerField(default=0)


    def __str__(self):
        return self.username


class alpha_category(models.Model):
    catname=models.CharField(max_length=25)
    cdis=models.CharField(max_length=30,unique=True)
    catimage=models.ImageField(upload_to='product/image',blank=True,null=True)


    def __str__(self):
        return self.catname










class alphaproducts1(models.Model):
    Userid=models.ForeignKey(alpha_signup,on_delete=models.CASCADE)
    productname=models.CharField(max_length=40)
    catname =models.ForeignKey(alpha_category,on_delete=models.CASCADE)
    pimage1 = models.ImageField(upload_to='product/image',blank=True,null=True,default='def_img.png')
    pimage2 = models.ImageField(upload_to='product/image', blank=True, null=True,default='def_img.png')
    pimage3 = models.ImageField(upload_to='product/image', blank=True, null=True,default='def_img.png')
    prize = models.IntegerField()
    sell = models.IntegerField()
    discount = models.IntegerField()
    brand=models.CharField(max_length=25)
    pdisc=models.CharField(max_length=50)
    spec_status=models.IntegerField(default=0)

    def __str__(self):
        return self.productname







class ramspec(models.Model):
    productid=models.ForeignKey(alphaproducts1,on_delete=models.CASCADE,default=1)
    ramtype=models.CharField(max_length=20)
    ramsize=models.IntegerField()
    ptotal = models.IntegerField()

    def __str__(self):
        return self.productid


class cameraspec(models.Model):
    productid=models.ForeignKey(alphaproducts1,on_delete=models.CASCADE,default=1)
    camresalution=models.CharField(max_length=30)
    camtype=models.IntegerField()
    ptotal = models.IntegerField()
    def __str__(self):
         return self.productid


class lapspec(models.Model):
    producid=models.ForeignKey(alphaproducts1,on_delete=models.CASCADE,default=1)
    ramdisc=models.CharField(max_length=30)
    ramsize = models.IntegerField()
    graphicsdisc = models.CharField(max_length=30)
    graphicssize = models.IntegerField()
    screensize = models.CharField(max_length=30)
    motherboard = models.CharField(max_length=30)
    hdd = models.IntegerField()
    sdd = models.IntegerField()
    systemos = models.CharField(max_length=30)
    processor = models.CharField(max_length=30)
    ptotal = models.IntegerField()


