from django.shortcuts import render
from django.http import HttpResponse
from registration.backends.simple.views import RegistrationView


def index(request):
    return render(request,'eventhub/base.html')

def about(request):
    return render(request,'eventhub/about.html')

def create(request):
    return render(request,'eventhub/create_event.html')

def recommended(request):
    return render(request,'eventhub/recommended.html')


#if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return '/eventhub/'
