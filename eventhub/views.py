from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from registration.backends.simple.views import RegistrationView
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from eventhub.models import Event, Pref, Like
from django.db.models import Q
from eventhub.forms import EventForm
from django.core.exceptions import ObjectDoesNotExist


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
    if request.method == "POST":
        p = request.POST
        for key, value in p.items():
            print(key, value)
        e = Event.objects.create(
                                category=p['category'],
                                title=p['title'],
                                loc=p['loc'],
                                creator=request.user,
                                datetime=p['datetime'],
                                desc=p['desc'],
                                pos=p['postcode'],
                                )
        return HttpResponseRedirect('/eventhub/event/'+str(e.id))
    else:
        active = ["","","","active","","",""]
        return render(request,'eventhub/create_event.html', context={'active':active, 'initVal':["","","","",""]})

def event(request, eventID):
    active = ["","","","","","",""]
    try:
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
    pref = Pref.objects.get(user=request.user).preference
    return HttpResponse(pref)

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
