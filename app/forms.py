from django import forms


class TimeForm(forms.Form):
    time = forms.TimeField(label='')
