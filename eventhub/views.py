from django.shortcuts import render
from django.http import HttpResponse
from registration.backends.simple.views import RegistrationView
from eventhub.models import Event

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

def event(request):
    return render(request, 'eventhub/event.html')

def recommended(request):
    return render(request,'eventhub/recommended.html')


#if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return '/eventhub/'
