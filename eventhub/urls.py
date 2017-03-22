from django.shortcuts import render
from django.conf.urls import url
from eventhub import views
from registration.backends.simple.views import RegistrationView

urlpatterns = [ url(r'^$', views.index, name='index'),
                url(r'about/$', views.about, name='about'),
                url(r'create_event/$', views.create, name='create'),
                url(r'event/(?P<eventID>[\w\-]+)/$', views.event, name='event'),
                url(r'search/(?P<search>[\w\-]+)/$', views.search, name='search'),
                url(r'category/(?P<cat>[\w\-]+)/$', views.category, name='category'),
                url(r'profile/', views.profile, name='profile'),
                url(r'creator/', views.get_creator, name='get_creator'),
                url(r'post_prefs/', views.post_prefs, name='post_prefs'),
                url(r'recommended/', views.recommended, name='recommended'),
            ]
