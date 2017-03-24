from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from registration.backends.simple.views import RegistrationView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import ensure_csrf_cookie
from eventhub.models import Event, Pref, Like
from django.db.models import Q
from eventhub.forms import EventForm
from django.core.exceptions import ObjectDoesNotExist
import dateutil.parser
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime, date, time
import re

@receiver(post_save, sender=User)
def userNew(sender, **kwargs):
    print('uhhh')

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

def eventValidator(postvars):
    if len(postvars['title']) > 15:
        return False
    if postvars['category'] == '':
        return False
    if not re.match(r"^[A-Z]{1,2}[0-9]{1,2} ?[0-9][A-Z]{2}$", postvars['postcode'].upper()):
        return False
    if datetime.now() > datetime.strptime(postvars['datetime'], "%Y-%m-%dT%H:%M"):
        return False
    if len(postvars['loc']) > 128:
        return False
    if len(postvars['desc']) > 1000:
        return False
    return True

def edit(request, eid):
    if request.method == "POST":
        p = request.POST
        e = Event.objects.get(id=eid)
        e.title = p['title']
        e.category = p['category']
        e.loc = p['loc']
        e.datetime = p['datetime']
        e.desc = p['desc']
        e.pos = p['postcode']
        e.save()
        return HttpResponseRedirect('/eventhub/event/'+eid)

    e = Event.objects.get(id=eid)
    x = str(e.datetime).split(' ')
    dt = x[0]+'T'+x[1][:5]
    initVal = {'title':e.title,'cat':e.category,'dt':dt,'pc':e.pos,'loc':e.loc,'desc':e.desc,'url':'/eventhub/edit/'+eid+'/'}
    return render(request,'eventhub/create_event.html', context={'active':["","","","","","",""], 'initVal':initVal, 'title':'Edit Event'})

def create(request):
    initVal = {'url':"/eventhub/create_event/"}
    if request.method == "POST":
        p = request.POST
        if eventValidator(p):
            e = Event.objects.create(
                                    category=p['category'],
                                    title=p['title'],
                                    loc=p['loc'],
                                    creator=request.user,
                                    datetime=p['datetime'],
                                    desc=p['desc'],
                                    pos=p['postcode'],
                                    )
            e.save()
            return HttpResponseRedirect('/eventhub/event/'+str(e.id))
        else:
            initVal['cat']=p['category']
            initVal['title']=p['title']
            initVal['loc']=p['loc']
            initVal['dt']=p['datetime']
            initVal['desc']=p['desc']
            initVal['pc']=p['postcode']
            initVal['error'] = '''The title should be shorter than 10 characters.<br/>
                                The category should be one of the categories.<br/>
                                The location should be shorter than 128 characters.<br/>
                                The date should be in the future.<br/>
                                The postcode should be a valid postcode.<br/>
                                The description should be less than 1000 characters.<br/>'''
    active = ["","","","active","","",""]
    return render(request,'eventhub/create_event.html', context={'active':active, 'initVal':initVal, 'title':'Create Event'})

def event(request, eventID):
    active = ["","","","","","",""]
    try:
        currentUser=request.user
        button = ''
        if currentUser.username != "":
            Like.objects.get(user=request.user,event=eventID)
            button = '<button id="like" type="button" class="btn btn-primary btn-lg active" onclick="removeLike('+eventID+')">Unlike</button>'
    except ObjectDoesNotExist:
        button = '<button id="like" type="button" class="btn btn-primary btn-lg" onclick="addLike('+eventID+')">Like</button>'
    e = Event.objects.get(id=eventID)
    pos = 'https://www.google.com/maps/embed/v1/place?q='+e.pos+'&key=AIzaSyAk67VAOhMC_8HSXADhnLSoFN1Al8b_tGU'
    return render(request, 'eventhub/event.html', context={'button':button, 'event': e, 'active':active, 'pos':pos, 'isCreator': (e.creator == request.user)})

def category(request, cat):
    active = ["","","","","","",""]
    events = Event.objects.filter(category=cat)
    return render(request, 'eventhub/browse.html', context={'events': events, 'title': 'Category: '+cat})

def search(request, search):
    active = ["","","","","","",""]
    title = 'Order by: '+search
    if search == 'date':
        events = Event.objects.order_by('datetime')
    elif search == 'location':
        events = Event.objects.order_by('loc')
    else:
        title = 'Looking for: '+search
        events = Event.objects.filter(Q(title__contains=search) | Q(loc__contains=search) | Q(category__contains=search))
    return render(request, 'eventhub/browse.html', context={'events': events, 'title': title})

def profile(request):
    active = ["","","","","active","",""]
    checked = ["checked","checked",""]
    currentUser = request.user
    events = Event.objects.filter(creator=currentUser)[:3]
    return render(request, 'eventhub/profile.html', context={'checked': checked, 'active': active, 'user':currentUser, 'events':events})

def post_event(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')
        else:
            form = EventForm()

    return render(request, 'create_event.html', {'form': form})

def get_creator(request):
    pref = Pref.objects.get_or_create(user=request.user)
    return HttpResponse(pref[0].preference)

@ensure_csrf_cookie
def post_prefs(request):
    p = Pref.objects.get(user=request.user)
    p.preference = request.POST.get("prefs","")
    p.save()
    return HttpResponse('Updated!')

def recommended(request):
    prefs = Pref.objects.get(user=request.user).preference.split(',')
    events = Event.objects.filter(category__in=prefs).order_by('-likes')[:6]
    return render(request, 'eventhub/browse.html', context={'title': 'Recommended Events:', 'events': events})

def add_like(request, eid):
    e = Event.objects.get(id=eid)
    e.likes += 1
    e.save()
    Like.objects.create(user=request.user, event=e).save()
    return HttpResponse("Successful")

def remove_like(request, eid):
    e = Event.objects.get(id=eid)
    e.likes -= 1
    e.save()
    Like.objects.get(user=request.user, event=eid).delete()
    return HttpResponse("Successful")

#if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return '/eventhub/'
