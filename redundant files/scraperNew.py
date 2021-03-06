from lxml import html
import requests
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

f = open('testData.txt', 'w')
f.write(str(final))
f.close()
