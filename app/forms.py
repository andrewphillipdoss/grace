from django.forms import ModelForm
from app.models import Person

class TimeForm(ModelForm):
    class Meta:
        model = Person
        fields = ['id','unique_time']
