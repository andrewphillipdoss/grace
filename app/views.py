from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

from .forms import TimeForm

# Create your views here.
def home_page(request):
    persons = Person.objects.all()
    if request.method == 'POST':
        form = TimeForm(request.POST)
        if form.is_valid():
            person = persons[form.fields['id']]
            person.unique_time = form.cleaned_data['unique_time']
            person.save()
            #return HttpResponse(request.POST['stop_time'])
    else:
        form = TimeForm()
    return render(request, 'home.html', {'persons': persons, 'form': form})
