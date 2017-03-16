import os
os.environ.setdefault('DJANGO_SETINGS_MODULE','WAD2group.settings')

import django
django.setup()
from eventhub.models import Category, eventhub

def populate():
    #simple events and categories until scraper gets made
    buisness_events = [{'name': 'Meeting'},
                       {'name': 'Brainstorm'}]

    educational_events = [{'name': 'Museum Trip'},
                          {'name': 'Lecture'},
                          {'name': 'Talk'}]

    music_events = [{'name': 'Concert'}]

    social_events = [{'name': 'Party'},
                     {'name': 'DnD Game'}]

    cats = {'Business': {'events': business_events},
            'Educational': {'events': educational_events},
            'Music': {'events': music_events},
            'Social': {'events': social_events}}

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for e in cat_data["events"]:
            add_event(c, e["name"])

def add_event(cat, name):
    e = Event.objects.get_or_create(category = cat, name = name)[0]
    e.save()
    return e

def add_cat(name):
    c = Category.objects.get_or_create(name = name)[0]
    c.save()
    return c

if __name__ == '__main__':
    print("Starting EventHub population script...")
    populate()
