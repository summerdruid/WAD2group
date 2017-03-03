from django.shortcuts import render
from django.conf.urls import url
from eventhub import views
from registration.backends.simple.views import RegistrationView

urlpatterns = [ url(r'^$', views.index, name='index'), ]
