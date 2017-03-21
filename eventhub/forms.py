from django import forms
from eventhub.models import Event
from eventhub.models import UserProfile

class EventForm(forms.ModelForm):

    category = forms.CharField(max_length = 32, help_text = "Please enter the category name.")
    title = forms.CharField(max_length = 256, help_text = "Please enter the title.")
    loc = forms.CharField(max_length = 128, help_text = "Please enter the location.")
    date = forms.DateField(widget=forms.DateInput( format = '%d/%m/%y'))
    time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))

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
