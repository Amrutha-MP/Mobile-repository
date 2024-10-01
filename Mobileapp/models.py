from django.db import models

# Create your models here.
class Mobile_Db(models.Model):
    Company_Name = models.CharField(max_length=50,null=True,blank=True)
    Description = models.CharField(max_length=50,null=True,blank=True)
    Company_Image = models.ImageField(upload_to="company pictures",null=True,blank=True)
class MobDb(models.Model):
    CompanyName=models.CharField(max_length=50,null=True,blank=True)
    Mobile_Name=models.CharField(max_length=50,null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    Description=models.CharField(max_length=50,null=True,blank=True)
    Mobile_Image1= models.ImageField(upload_to="mobile pictures",null=True,blank=True)
    Mobile_Image2= models.ImageField(upload_to="mobile pictures", null=True, blank=True)
    Mobile_Image3= models.ImageField(upload_to="mobile pictures", null=True, blank=True)