import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','WAD2group.settings')

import django
django.setup()
from eventhub.models import Category, Event

from lxml import html
import requests

def populate():
    categories = ["business", "educational", "music", "social"]
    results = {'business': {}, 'educational': {}, 'music': {}, 'social': {}}

    for cat in categories:
        p = 0
        while True:
            p += 1
            site = 'http://glasgow.eventful.com/atom/events?q=' + cat + '&ga_search=music&ga_type=events&sort_order=Date&page_number=' + str(
                p)
            page = requests.get(site).content
            tree = html.fromstring(page)
            if int(tree.xpath('//totalresults')[0].text) == 0:
                break
            titles = [e.text.encode('utf-8') for e in tree.xpath('//feed/entry/title')]
            loc = [e.text.encode('utf-8') for e in tree.xpath('//feed/entry/where/entrylink/entry/title')]
            pos = [e.text.encode('utf-8') for e in tree.xpath('//feed/entry/where/point/pos')]

            for i in range(len(titles)):
                results[cat][titles[i]] = {'loc': loc[i], 'pos': pos[i]}

        print("loading...")

    for cat in categories:
        c = add_cat(cat)
        print("loading...")
        for title in results[cat]:
            e = add_event(c, title, results[cat][title]['loc'], results[cat][title]['pos'])

    for c in Category.objects.all():
        print(str(c) + ":")
        for e in Event.objects.filter(category = c):
            print("- " + str(e))

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
