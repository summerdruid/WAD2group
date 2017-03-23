import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','WAD2group.settings')
import sys
import django
django.setup()
from eventhub.models import Event, UserProfile
from django.contrib.auth.models import User
from random import randint

from lxml import html
import requests

def populate():
    users = create_users(["Adam", "Ben", "Claire", "David", "Elaine"])
    #f = open('testData.txt', 'r')
    #results = eval(f.readline())
    #f.close()
    final = {}

    for eventType in ['parties', 'music', 'business']:
        site = 'https://www.eventbrite.com/d/united-kingdom--glasgow/'+ eventType +'/?crt=regular&page=1&sort=best'
        page = requests.get(site).content
        tree = html.fromstring(page)

        titles = [t.text[17:-18] for t in tree.xpath("//div[@class='list-card__title']")]
        place = [t.text[18:-18] for t in tree.xpath("//div[@class='list-card__venue']")]
        date = []
        time = []

        results = {}

        times = tree.xpath("//time[@class='list-card__date']")
        for t in times:
            x = t.text
            if x[34] == ' ' and x[33] == ' ':
                date.append(x[23:33])
                time.append(x[55:63])
            elif x[34] == ' ':
                date.append(x[23:33])
                time.append(x[54:62])
            else:
                date.append(x[23:33])
                time.append(x[53:61])

        print(titles[0])
        for i in range(len(titles)):
            results[titles[i]] = {'loc': place[i], 'date': date[i], 'time': time[i]}
        if eventType == 'parties':
            final['social'] = results
        else:
            final[eventType] = results

    for cat in final:
        print("loading...")
        for title in final[cat]:
            i = randint(0,4)
            e = add_event(cat, title, final[cat][title]['loc'], final[cat][title]['date'],
                          final[cat][title]['time'], users[i])

    for c in final:
        for e in Event.objects.filter(category = c):
            print(str(e))

def add_event(cat, title, loc, date, time, creator):
    e = Event.objects.get_or_create(category = cat, title = title, loc = loc, date = date,
                                    time = time, creator = creator)[0]
    e.save()
    return e

def create_users(names):
    users = []
    for n in names:
        user = User.objects.get_or_create(username = n, password = "password")[0]
        u = UserProfile.objects.get_or_create(user = user)[0]
        u.save()
        users.append(u)
    return users


#def add_cat(name):
    #c = Category.objects.get_or_create(name = name)[0]
    #c.save()
    #return c

if __name__ == '__main__':
    print("Starting EventHub population script...")
    populate()
