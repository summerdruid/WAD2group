from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 128, unique = True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Event(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length = 128)
    loc = models.CharField(max_length = 128)
    pos = models.CharField(max_length = 128)
    #creator = models.ForeignKey(UserProfile)
    #date=...


    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return  self.user.username
