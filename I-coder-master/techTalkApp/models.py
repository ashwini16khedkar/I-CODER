from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.conf import settings
# Create your models here.

class Gender(models.Model):
    gender = models.CharField(max_length=10,null=False,blank=False)

class UserProfile(models.Model):
    user_id = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.PROTECT)
    profile_photo = models.ImageField(upload_to='user_profile/images',blank=True,null=True)
    gender = models.ForeignKey(Gender,on_delete=models.PROTECT,blank=True,null=True)
    phone = models.CharField(max_length=20,blank=True,null=True)

class ContactUs(models.Model):
    name = models.CharField(max_length=30,blank=False,null=False)
    email = models.EmailField(max_length=50,blank=False,null=False)
    message = models.CharField(max_length=300,blank=False,null=False)

class Comments(models.Model):
    comments = models.CharField(max_length=200,blank=False,null=False)
    commented_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT,blank=False,null=False)

class Images(models.Model):
    image = models.ImageField(upload_to='article/images',blank=False,null=False)

class Likes(models.Model):
    likes_count = models.IntegerField(default=0)
    like_by = models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True)

class Article(models.Model):
    title = models.CharField(max_length=60,blank=False,null=False)
    datetime = models.DateTimeField()
    auther = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, blank=False, null=False)
    likes = models.ForeignKey(Likes, on_delete=models.PROTECT, blank=False, null=False)
    article = models.CharField(max_length=1000,blank=False,null=False)
    comments = models.ManyToManyField(Comments,blank=True)
    article_images = models.ManyToManyField(Images,blank=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        self.title

