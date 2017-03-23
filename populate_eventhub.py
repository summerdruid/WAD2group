import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','WAD2group.settings')
import sys
import django
django.setup()
from eventhub.models import Event
from django.contrib.auth.models import User
def populate():
    events={ 'title':[
      'Pool night',
      'Vulfpeck concert',
      'Tesco: management seminar',
      'Chess fun with Ali Munn',
      'Argos: Sales meeting',
      'Susan Boyle Live at the Hydro',
      ], 'category':[
      'social',
      'music',
      'business',
      'social',
      'business',
      'music'], 'position':[
      'G12 8LX',
      'G12 8LX',
      'G12 8LX',
      'G12 8LX',
      'G12 8LX',
      'G12 8LX'], 'location':[
      'Glasgow University Union',
      'Flying Duck Bar',
      'Tesco Stores',
      'Queen Margaret Union',
      'Argos stores',
      'The Hydro'], 'description':[
      'Weekly pool night-bring £2',
      'Vulfpeck finally in Scotland!',
      'Details have been emailed to your staff email',
      'Tutoring night for Chess',
      'Details have been emailed to your staff email',
      'Knock your socks off!'],'creator':[
      'Michael',
      'Cameron',
      'Dominic',
      'Mary',
      'Michael',
      'Cameron'],'datetime':[
      '2017-04-13 18:30:00',
      '2017-05-15 19:30:00',
      '2017-04-03 14:00:00',
      '2017-04-02 18:30:00',
      '2017-04-17 10:00:00',
      '2017-06-17 19:00:00']}

    for i in range(0,6):
        e=Event.objects.create(category=events['category'][i],title=events['title'][i],loc=events['location'][i],pos=events['position'][i],creator=User.objects.get(username=events['creator'][i]),datetime=events['datetime'][i],desc=events['description'][i])
        e.save()
populate()
