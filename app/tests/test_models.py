from django.test import TestCase
from app.models import Person

class PersonModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Person.objects.create(
            type='A', label= 'pedestrian', name='Jerry Crunch',
            eligible=True, unique_time=null, sandwiches=null,
            stop_time=null
        )

    def test_unique_time_label(self):
        person = Person.objects.get(id=1)
        field_label = person._meta.get_field('unique_time').verbose_name
        assertEquals(field_label, 'unique time')

    def test_stop_time_label(self):
        person = Person.objects.get(id=1)
        field_label = person._meta.get_field('stop_time').verbose_name
        assertEquals(field_label, 'stop time')
