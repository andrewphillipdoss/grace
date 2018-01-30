from django.db import models
from django.utils import timezone
import django.dispatch
import datetime
import math

# Create your models here.
class Person(models.Model):

    type_person = models.CharField(
        max_length=1,
        choices=(('A','A'),('B','B'),('C','C'),('D','D'))
        )
    name = models.CharField(max_length=50)
    label = models.CharField(max_length=30)
    eligible = models.BooleanField()
    unique_time = models.TimeField(blank=True, null=True)
    sandwiches = models.PositiveSmallIntegerField(null=True)
    stop_time = models.TimeField(blank=True, null=True)

    def setUp(self):
        if self.eligible == False:
            self.unique_time == None
            self.sandwiches == None
        self.calculateSandwiches()

    def resetStop(self):
        self.stop_time = None

    def calculateSandwiches(self):
        self.sandwiches = None
        if self.eligible == True and self.stop_time == None and self.unique_time != None:
            now = datetime.datetime.time(datetime.datetime.now())
            unique_milli = 1000.0 * ((self.unique_time.hour)*60*60 + (self.unique_time.minute)*60 + self.unique_time.second)
            now_milli = 1000.0 * (now.hour*60*60 + now.minute*60 + now.second + now.microsecond/(1e6))
            interval_milli = 21600000 + 720000 #6 hours and 12 minutes in milliseconds
            sand_num = max(0, math.ceil((now_milli - unique_milli - interval_milli) / (1000.0*60*30)))
            self.sandwiches = sand_num

    def __unicode__(self):
        return self.establishment
