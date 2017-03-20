from django.shortcuts import render
from django.http import HttpResponse
from registration.backends.simple.views import RegistrationView


def index(request):
    return render(request,'eventhub/base.html')


#if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return '/eventhub/'
def change_password(request):
    return render(request, 'eventhub/password_change_form.html')
