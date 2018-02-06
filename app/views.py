from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from app.models import *
from django.utils.encoding import smart_str
import csv
from .forms import TimeForm

# use this line to debug:
# import pdb; pdb.set_trace()

class MainPageView(TemplateView):
    template_name = "home.html"
    form = TimeForm
    persons = Person.objects.all()

    def get(self, request, *args, **kwargs):
        persons = self.persons
        form = self.form()
        for person in persons:
            Person.setUp(person)
            Person.calculateSandwiches(person)
        return render(request, self.template_name, {'persons': persons, 'form': form})

    def post(self, request):
        body = request.body
        persons = self.persons

        #Create array for which persons have been selected
        persons_selected = []
        for i in range(0, persons.count()):
            if request.POST.get(str(i)) is not None:
                persons_selected.append(persons[int(request.POST[str(i)])])
        print(persons_selected)

        input_type = request.POST['type']
        form = self.form(request.POST)
        if form.is_valid():
            if input_type == 'unique_select':
                for person_selected in persons_selected:
                    if person_selected.eligible:
                        person_selected.unique_time = form.cleaned_data['time']
                        Person.resetStop(person_selected)
                        Person.calculateSandwiches(person_selected)
                        person_selected.save()
            elif input_type == 'stop_select':
                for person_selected in persons_selected:
                    person_selected.stop_time = form.cleaned_data['time']
                    Person.calculateSandwiches(person_selected)
                    person_selected.save()
            elif input_type == 'unique':
                person = persons[int(request.POST['pk'])-1]
                person.unique_time = form.cleaned_data['time']
                Person.resetStop(person)
                Person.calculateSandwiches(person)
                person.save()
            elif input_type == 'stop':
                person = persons[int(request.POST['pk'])-1]
                person.stop_time = form.cleaned_data['time']
                Person.calculateSandwiches(person)
                person.save()
            else:
                pass
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
        (u"Name"),
        smart_str(u"Label"),
        smart_str(u"Unique"),
        smart_str(u"Sandwiches"),
        smart_str(u"Stop")
    ])
    #get data from database or from text file
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
