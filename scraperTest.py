from lxml import html
import requests

categories = ["business", "educational", "music", "social"]
results = {'business': {}, 'educational': {}, 'music': {}, 'social': {}}

for cat in categories:
    p = 0
    while True:
        p += 1
        site = 'http://glasgow.eventful.com/atom/events?q='+cat+'&ga_search='+cat+'&ga_type=events&sort_order=Date&page_number=' + str(p)
        page = requests.get(site).content
        tree = html.fromstring(page)
        if int(tree.xpath('//totalresults')[0].text) == 0:
            break
        titles = [e.text.encode('utf-8') for e in tree.xpath('//feed/entry/title')]
        loc = [e.text.encode('utf-8') for e in tree.xpath('//feed/entry/where/entrylink/entry/title')]
        pos = [e.text.encode('utf-8') for e in tree.xpath('//feed/entry/where/point/pos')]

        for i in range(len(titles)):
            results[cat][titles[i]] = {'loc': loc[i], 'pos': pos[i]}

        print(p)

for cat in categories:
    print (cat + ":")
    for title in results[cat]:
        print(title + ": " + str(results[cat][title]))
