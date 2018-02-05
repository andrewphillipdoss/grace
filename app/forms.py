from django import forms

class TimeForm(forms.Form):
    time = forms.TimeField(widget=forms.TextInput(attrs={'class' : 'form-control', 'type': 'time'}), label='')
