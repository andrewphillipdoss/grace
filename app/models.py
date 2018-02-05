from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save
from django.dispatch import receiver
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
    unique_date = models.DateField(auto_now=True)
    sandwiches = models.PositiveSmallIntegerField(null=True)
    stop_time = models.TimeField(blank=True, null=True)

    # ensure only those eligible have unique or sandwiches
    def setUp(self):
        if self.eligible == False:
            self.unique_time == None
            self.sandwiches == None

    def resetStop(self):
        self.stop_time = None

    def calculateSandwiches(self):
        if self.sandwiches == 0 or self.unique_time == None:
            self.sandwiches = None
        elif self.eligible == True and self.stop_time == None and self.unique_time != None:
            now = datetime.datetime.now()
            now_milli = now.timestamp() * 1000
            unique_milli = datetime.datetime.combine(self.unique_date, self.unique_time).timestamp() * 1000
            interval_milli = 21600000 + 720000 #6 hours and 12 minutes in milliseconds
            sand_num = max(0, math.ceil((now_milli - unique_milli - interval_milli) / (1000.0*60*30)))
            self.sandwiches = sand_num

    def __unicode__(self):
        return self.establishment

# Use this to update the unique_date as the date
# when unique_time is updated
@receiver(pre_save)
def updateDates(sender, instance, **kwargs):
    old_instance = Person.objects.get(pk=instance.pk)
    if old_instance.unique_time != instance.unique_time:
        instance.unique_date = datetime.datetime.now().date()
