from django import forms
from .models import Bus

class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = ['routes', 'description', 'price', 'durations','person', 'date']