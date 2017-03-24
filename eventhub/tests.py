from django.core.urlresolvers import reverse
from django.test import TestCase
from django.conf import settings
from eventhub.models import Event
from eventhub.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from eventhub import views
def create_user():
    #creates a user for other tests
    user = User.objects.get_or_create(
                                        username="testuser",
                                        email="testuser@testuser.com",
                                        password="test1234",
                                        )[0]
    user.set_password(user.password)
    user.save()

    return user

class eventhub_tests(TestCase):

    def test_login_links(self):
        #testing that certain links can be seen when logged in
        #login as a user with create_user
        create_user()
        self.client.login(username='testuser', password='test1234')
        #get the url of index using urls.py name
        response=self.client.get(reverse('index'))
        #check for links when logged in
        self.assertIn(reverse('create'), response.content.decode('utf-8'))
        self.assertIn(reverse('recommended'), response.content.decode('utf-8'))

    def test_not_logged_in_links(self):
        #test links without login
        response=self.client.get(reverse('index'))
        #check which links are here and which ones aren't
        self.assertIn(reverse('registration_register'), response.content.decode('utf-8'))
        self.assertIn(reverse('auth_login'), response.content.decode('utf-8'))
        self.assertNotIn(reverse('recommended'), response.content.decode('utf-8'))
        self.assertNotIn(reverse('create'), response.content.decode('utf-8'))

    def test_create_an_event_show_in_profile(self):
        #checking event shown in profile
        create_user()
        self.client.login(username='testuser', password='test1234')
        #get profile of user
        response=self.client.get(reverse('profile'))
        u=User.objects.get(username='testuser')
        #create an event
        event=Event.objects.create(
                                    category='music',
                                    title='Jazz night',
                                    loc='Jazz bar',
                                    creator=u,
                                    datetime='2017-04-13 18:30:00',
                                    desc='Chilled night',
                                    pos='G12 0PR',
                                    )
        #save to database
        event.save()
        #check it is in database
        self.assertEquals(event,Event.objects.get(id=str(event.id)))


        #Does it display on profile?
        self.assertIn(reverse('eventhub/event/'+str(event.id)), response.content.decode('utf-8'))

    def test_like_event(self):
        create_user()
        self.client.login(username='testuser', password='test1234')
        u=User.objects.get(username='testuser')
        event=Event.objects.create(
                                    category='music',
                                    title='Jazz night',
                                    loc='Jazz bar',
                                    creator=u,
                                    datetime='2017-04-13 18:30:00',
                                    desc='Chilled night',
                                    pos='G12 0PR'
                                    )
        event.save()
        eid=event.id
        #go to add_like page
        u.client.get(reverse('add_like'))
        e=Event.objects.get(id=eid)
        #check that a like has been given to the event
        self.assertEquals(e.likes,1)

    def navigate_to_categories(self):
        response=self.client.get(reverse('index'))
        #check that the categories are in the index page
        self.assertIn(reverse('eventhub/category/music/'))
        self.assertIn(reverse('eventhub/category/social/'))
        self.assertIn(reverse('eventhub/category/business/'))
