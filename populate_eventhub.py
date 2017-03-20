import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','WAD2group.settings')
import sys
import django
django.setup()
from eventhub.models import Category, Event

from lxml import html
import requests

def populate():
    categories = ["business", "educational", "music", "social"]
    f = open('testData.txt', 'r')
    results = eval(f.readline())
    f.close()

    for cat in categories:
        c = add_cat(cat)
        print("loading...")
        for title in results[cat]:
            e = add_event(c, title, results[cat][title]['loc'], results[cat][title]['pos'])

    for c in Category.objects.all():
        print(str(c) + ":")
        for e in Event.objects.filter(category = c):
            print("- ",e)

def add_event(cat, title, loc, pos):
    e = Event.objects.get_or_create(title = title, loc = loc, pos = pos)[0]
    if e.category == None:
        e.category = cat
    e.save()
    return e

def add_cat(name):
    c = Category.objects.get_or_create(name = name)[0]
    c.save()
    return c

if __name__ == '__main__':
    print("Starting EventHub population script...")
    populate()
