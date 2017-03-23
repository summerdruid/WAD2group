from django import forms
from eventhub.models import Event
from eventhub.models import User

class EventForm(forms.ModelForm):

    category = forms.CharField(max_length = 32, label = "Please enter the category name.", required=True)
    title = forms.CharField(max_length = 256, label = "Please enter the title.", required=True)
    loc = forms.CharField(max_length = 128, label = "Please enter the location.", required=True)
    datetime = forms.DateTimeField(label = "Enter the date and time of your event.", required=True)

    class Meta:
        model = Event
        exclude = ['creator', 'likes']
