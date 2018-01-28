from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib import messages
from app.models import *
from django.utils.encoding import smart_str
import csv

from .forms import TimeForm

class MainPageView(TemplateView):
    template_name = "home.html"
    template2 = "test.html"
    form = TimeForm
    persons = Person.objects.all()
    persons_filter = Person.objects.all().distinct()

    def get(self, request, *args, **kwargs):
        persons = self.persons
        persons_filter = self.persons_filter
        form = self.form()
        for person in persons:
            Person.setUp(person)
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
                Person.resetStop(person)
            else:
                person.stop_time = form.cleaned_data['time']
            Person.calculateSandwiches(person)
        return render(request, self.template_name, {'persons': persons, 'form': form})


# generate and download csv file
def download_csv_data(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="grace.csv"'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8'))

    #write the headers
    writer.writerow([
        smart_str(u"Type"),
        smart_str(u"Name"),
        smart_str(u"Label"),
        smart_str(u"Unique"),
        smart_str(u"Sandwiches"),
        smart_str(u"Stop")
    ])
    #get data from database or from text file....
    persons = Person.objects.all()
    for person in persons:
        writer.writerow([
            smart_str(person.type_person),
            smart_str(person.name),
            smart_str(person.label),
            smart_str(person.unique_time),
            smart_str(person.sandwiches),
            smart_str(person.stop_time)
        ])
    return response
