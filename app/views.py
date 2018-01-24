from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from app.models import *

from .forms import TimeForm

class MainPageView(TemplateView):
    template_name = "home.html"
    template2 = "test.html"
    form = TimeForm
    persons = Person.objects.all()

# Create your views here.
    def get(self, request, *args, **kwargs):
        persons = self.persons
        form = self.form()
        return render(request, self.template_name, {'persons': persons, 'form': form})

    def post(self, request):
        body = request.body
        persons = self.persons
        person = persons[int(request.POST['pk'])-1]
        input_type = request.POST['type']
        form = self.form(request.POST)
        if form.is_valid():
            if input_type == 'unique':
                person.unique_time = form.cleaned_data['time']
            else:
                person.stop_time = form.cleaned_data['time']
            Person.calculateSandwiches(person)
            person.save()
        return render(request, self.template_name, {'persons': persons, 'form': form})
