from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    category = models.CharField(max_length = 32)
    title = models.CharField(max_length = 256)
    loc = models.CharField(max_length = 128)
    pos = models.CharField(max_length = 128)
    creator = models.ForeignKey(User)
    datetime = models.DateTimeField()
    desc = models.CharField(max_length = 1024, null = True)
    likedBy = models.CharField(max_length = 1024, null = True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

class Pref(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preference = models.CharField(max_length=22)
