from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 128, unique = True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Event(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length = 128, unique = True)
    creator = models.ForeignKey(UserProfile)

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
