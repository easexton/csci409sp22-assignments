from django import forms

class FlightForm(forms.Form):
    origin = forms.CharField(label='Origin Airport')
    destination = forms.CharField(label='Destination Airport')