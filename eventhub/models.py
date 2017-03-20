from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return  self.user.username

class Event(models.Model):
    category = models.CharField(max_length = 32)
    title = models.CharField(max_length = 256)
    loc = models.CharField(max_length = 128)
    creator = models.ForeignKey(UserProfile)
    date = models.CharField(max_length = 32)
    time = models.CharField(max_length = 32)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
