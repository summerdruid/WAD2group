from django.core.urlresolvers import reverse
from django.test import TestCase
from django.conf import settings
from eventhub.models import Event
import os.path

def create_user():
    # Create a user
    from eventhub.models import User
    user = User.objects.get_or_create(
                                        username="testuser",
                                        email="testuser@testuser.com",
                                        password="test1234",
                                        )[0]
    user.set_password(user.password)
    user.save()

    return user

class eventhub_tests(TestCase):
    def test_not_logged_in_links(self):
        response=self.client.get(reverse('index'))
        self.assertIn(reverse('registration_register'), response.content.decode('utf-8'))
        self.assertIn(reverse('auth_login'), response.content.decode('utf-8'))
        self.assertNotIn(reverse('recommended'), response.content.decode('utf-8'))
        self.assertNotIn(reverse('create'), response.content.decode('utf-8'))

    def test_login_links(self):
        create_user()
        self.client.login(username='testuser', password='test1234')

        response = self.client.get(reverse('index'))
        #print(response.content.decode('utf-8'))
        self.assertIn(reverse('create'), response.content.decode('utf-8'))
        self.assertIn(reverse('recommended'), response.content.decode('utf-8'))

    def test_create_an_event_show_in_profile(self):
        create_user()
        self.client.login(username='testuser', password='test1234')
        response=self.client.get(reverse('profile'))

        event=Event.objects.create(
                                    category='music',
                                    title='Jazz night',
                                    loc='Jazz bar',
                                    creator=currentUser,
                                    datetime='2017-04-13 18:30:00',
                                    desc='Chilled night',
                                    pos='G12 0PR',
                                    )[0]
        event.save()
        self.assertEquals(event,Event.objects.get(id=str(event.id)))


        #Does it display on profile?
        self.assertIn(reverse('eventhub/event/'+str(event.id)), response.content.decode('utf-8'))

    def test_like_event(self):
        create_user()
        self.client.login(username='testuser', password='test1234')
        event=Event.objects.create(
                                    category='music',
                                    title='Jazz night',
                                    loc='Jazz bar',
                                    creator=currentUser,
                                    datetime='2017-04-13 18:30:00',
                                    desc='Chilled night',
                                    pos='G12 0PR'
                                    )[0]
        event.save()
        eid=event.id
        event.client.get(reverse('add_like'))
        e=Event.objects.get(id=eid)
        self.assertEquals(e.likes,1)

    def navigate_to_categories(self):
        response=self.client.get(reverse('index'))
        self.assertIn(reverse('eventhub/category/music/'))
        self.assertIn(reverse('eventhub/category/social/'))
        self.assertIn(reverse('eventhub/category/business/'))
