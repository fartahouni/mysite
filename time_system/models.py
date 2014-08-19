# -*- coding: utf-8 -*-​

from django.contrib.auth.models import User
from django.db import models
# Create your models here.


class To_Do_Pack(models.Model):
    title = models.CharField(max_length= 30)
    date = models.DateField(auto_now=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return u'%s - %s' %(self.title,self.user)


class To_Do(models.Model):
    title = models.CharField(max_length= 50)
    to_do_pack = models.ForeignKey(To_Do_Pack)
    start_time = models.TimeField()
    end_time = models.TimeField(null=True, blank=True)


    def __unicode__(self):
        return self.title

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    phoneNumber = models.CharField(u'شماره تلفن', blank=True , max_length=11)
    image = models.FileField(u'تصویر پروفایل', upload_to='/Users/farzanehtahooni/Documents/Arsh/ToDos/mysite/templates/static/profile_image',
                             blank=True, null=True,default='default')

    def __unicode__(self):
        return self.user.username