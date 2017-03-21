from django.shortcuts import render
from django.http import HttpResponse
from registration.backends.simple.views import RegistrationView
from eventhub.models import Event
from django.db.models import Q

def index(request):
    music = Event.objects.filter(category="music")[:3]
    business = Event.objects.filter(category="business")[:3]
    social = Event.objects.filter(category="social")[:3]
    contdict = {'events': {'music': music, 'business': business, 'social': social}}

    return render(request,'eventhub/index.html', context=contdict)

def about(request):
    return render(request,'eventhub/about.html')

def create(request):
    return render(request,'eventhub/create_event.html')

def event(request, eventID):
    e = Event.objects.get(id=eventID)
    return render(request, 'eventhub/event.html', context={'event': e})

def recommended(request):
    return render(request,'eventhub/recommended.html')

def category(request, cat):
    events = Event.objects.filter(category=cat)
    return render(request, 'eventhub/browse.html', context={'events': events, 'title': 'Category: '+cat})

def search(request, search):
    events = Event.objects.filter(Q(title__contains=search) | Q(loc__contains=search) | Q(category__contains=search))
    return render(request, 'eventhub/browse.html', context={'events': events, 'title': 'Looking for: '+search})
    
def profile(request):
    currentuser = request.user
    return(currentuser)

#if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return '/eventhub/'
