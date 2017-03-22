from django.shortcuts import render
from django.http import HttpResponse
from registration.backends.simple.views import RegistrationView
from django.contrib.auth.decorators import login_required
from eventhub.models import Event
from django.db.models import Q


def index(request):
    music = Event.objects.filter(category="music")[:3]
    business = Event.objects.filter(category="business")[:3]
    social = Event.objects.filter(category="social")[:3]
    active = ["active","","","","","",""]
    contdict = {'events': {'music': music, 'business': business, 'social': social}, 'active':active}

    return render(request,'eventhub/index.html', context=contdict)

def about(request):
    active = ["","active","","","","",""]
    return render(request,'eventhub/about.html', context={'active':active})

def create(request):
    active = ["","","","active","","",""]
    return render(request,'eventhub/create_event.html', context={'active':active})

def event(request, eventID):
    active = ["","","","","","",""]
    e = Event.objects.get(id=eventID)
    p = e.pos.split(',')
    pos = 'https://www.google.com/maps/embed/v1/place?q='+p[0]+'%2C'+p[1]+'&key=AIzaSyAk67VAOhMC_8HSXADhnLSoFN1Al8b_tGU'
    return render(request, 'eventhub/event.html', context={'event': e, 'active':active, 'pos':pos})

def category(request, cat):
    active = ["","","","","","",""]
    events = Event.objects.filter(category=cat)
    return render(request, 'eventhub/browse.html', context={'events': events, 'title': 'Category: '+cat})

def search(request, search):
    active = ["","","","","","",""]
    events = Event.objects.filter(Q(title__contains=search) | Q(loc__contains=search) | Q(category__contains=search))
    return render(request, 'eventhub/browse.html', context={'events': events, 'title': 'Looking for: '+search})

def profile(request):
    active = ["","","","","active","",""]
    currentUser = request.user
    events = Event.objects.filter(creator=currentUser)[:3]
    return render(request, 'eventhub/profile.html', context={'active': active, 'user':currentUser, 'events':events})

#if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return '/eventhub/'
