from django.test import TestCase
from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.urlresolvers import reverse
import os

from django.contrib.staticfiles import finders

#import populate_eventhub
import test_utils

from django.template import loader
from django.conf import settings
import os.path

from eventhub.models import User, UserProfile
from eventhub.forms import UserForm, UserProfileForm
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files.storage import default_storage

class IndexPageTests(TestCase):
        
    def test_index_contains(self):
      
        response = self.client.get(reverse('index'))
        self.assertIn(b'Rango says', response.content)
        
    def test_index_using_template(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'eventhub/index.html')

    def test_index_contains_link_to_about_page(self):
        try:
            response = self.client.get(reverse('about'))
        except:
            try:
                response = self.client.get(reverse('eventhub:about'))
            except:
                return False

        self.assertIn('href="' + reverse('About') + '"', response.content)
        
    def test_index_contains_link_to_recommended_page(self):
        # Access index
        try:
            response = self.client.get(reverse('recommended'))
        except:
            try:
                response = self.client.get(reverse('eventhub:recommended'))
            except:
                return False

        self.assertIn('href="' + reverse('Recommended') + '"', response.content)
        
    def test_index_contains_link_to_create_event_page(self):
        try:
            response = self.client.get(reverse('create_event'))
        except:
            try:
                response = self.client.get(reverse('eventhub:create_event'))
            except:
                return False

       
        self.assertIn('href="' + reverse('Create Event') + '"', response.content)

    def test_index_contains_link_to_sign_in(self):
        # Access index
        try:
            response = self.client.get(reverse('login'))
        except:
            try:
                response = self.client.get(reverse('eventhub:login'))
            except:
                return False

        
        self.assertIn('href="' + reverse('login') + '"', response.content)

    def test_index_contains_link_to_sign_in(self):
        # Access index
        try:
            response = self.client.get(reverse('register'))
        except:
            try:
                response = self.client.get(reverse('eventhub:register'))
            except:
                return False

        
        self.assertIn('href="' + reverse('register') + '"', response.content)
    

class AboutPageTests(TestCase):
        
    def test_about_contains_create_message(self):
        response = self.client.get(reverse('about'))
        self.assertIn(b'Welcome to eventhub', response.content)
        
class ModelTests(TestCase):

    def test_create_a_new_event(self):
        event = Event(name="ScottishChampionships")
        cat.save()

        # Check category is in database
        categories_in_database = Event.objects.all()
        self.assertEquals(len(Event_in_database), 1)
        only_poll_in_database = Event_in_database[0]
        self.assertEquals(only_poll_in_database,event)
    
class ViewTests(TestCase):

    def test_base_template_exists(self):
        # Check base.html exists inside template folder
        basepath= settings.TEMPLATE_DIR + '/eventhub/base.html'
        self.assertTrue(os.path.isfile(basepath))

    def test_titles_displayed(self):
        # Create user and log in
        test_utils.create_user()
        self.client.login(username='testuser', password='test1234')

        # Create event
        categories = test_utils.create_event()#needs to be changed

        # Access index and check the title displayed
        response = self.client.get(reverse('index'))
        self.assertIn('Rango -'.lower(), response.content.lower())
    def test_registration_form_is_displayed_correctly(self):
        #Access registration page
        try:
            response = self.client.get(reverse('register'))
        except:
            try:
                response = self.client.get(reverse('eventhub:register'))
            except:
                return False


        self.assertIn('<strong>Register here</strong><br />'.lower(), response.content.lower())

        # Check form in response context is instance of UserForm
        self.assertTrue(isinstance(response.context['user_form'], UserForm))

        # Check form in response context is instance of UserProfileForm
        self.assertTrue(isinstance(response.context['profile_form'], UserProfileForm))

        user_form = UserForm()
        profile_form = UserProfileForm()

        # Check form is displayed correctly
        self.assertEquals(response.context['user_form'].as_p(), user_form.as_p())
        self.assertEquals(response.context['profile_form'].as_p(), profile_form.as_p())

        # Check submit button
        self.assertIn('type="submit" name="submit" value="Register"', response.content)

    
    def test_login_form_is_displayed_correctly(self):
        #Access login page
        try:
            response = self.client.get(reverse('login'))
        except:
            try:
                response = self.client.get(reverse('rango:login'))
            except:
                return False

        #Check form display
        #Header
        self.assertIn('<h1>Login to Rango</h1>'.lower(), response.content.lower())

        #Username label and input text
        self.assertIn('Username:', response.content)
        self.assertIn('input type="text" name="username" value="" size="50"', response.content)

        #Password label and input text
        self.assertIn('Password:', response.content)
        self.assertIn('input type="password" name="password" value="" size="50"', response.content)

        #Submit button
        self.assertIn('input type="submit" value="submit"', response.content)

#login
#logout
#proper password/username
#each page has a template
#add an event
#like an event
#
