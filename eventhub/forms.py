from django import forms
from eventhub.models import Event
from eventhub.models import UserProfile

class EventForm(forms.ModelForm):

    category = forms.CharField(max_length = 32, help_text = "Please enter the category name.", required)
    title = forms.CharField(max_length = 256, help_text = "Please enter the title.", required)
    loc = forms.CharField(max_length = 128, help_text = "Please enter the location.")
    datetime = forms.DateTimeField(help_text = "Enter the date and time of your event.", required)

    class Meta:

        model = Event
        exclude = ('creator')

class PreferencesForm(forms.ModelForm):
     OPTIONS = (
                ("Music", "Music"),
                ("Business", "Business"),
                ("Social", "Social"),
                )
        Preferences = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                             choices=OPTIONS)
