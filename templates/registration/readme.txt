chapter11, things to do:

pip install -U django-resgistration-redux==1.4

add 'registration' in INSTALLED_APPS(setting.py file)
REGISTRATION_OPEN = True
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True
LOGIN_REDIRECT_URL = '/eventhub/'
LOGIN_URL = '/accounts/login/'  


add in project url:url(r'^accounts/', include('registration.backends.simple.urls')), #not app
from registration.backends.simple.views import RegistrationView (import to views too)

in views: add
class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return '/eventhub/'


in project url: add
  url(r'^accounts/register/$', views.MyRegistrationView.as_view(), name='registration_register'),