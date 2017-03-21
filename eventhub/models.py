from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    preferences = models.CharField(max_length = 256, null = True, blank = True)

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return  self.user.username

class Event(models.Model):
    category = models.CharField(max_length = 32)
    title = models.CharField(max_length = 256)
    loc = models.CharField(max_length = 128)
    pos = models.CharField(max_length = 528)
    creator = models.ForeignKey(UserProfile)
    datetime = models.DateTimeField()
    desc = models.CharField(max_length = 1024, null = True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
