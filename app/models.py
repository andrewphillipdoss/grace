from django.db import models
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

    def calculateSandwiches(self):
        unique = self.unique_time.hour*60*60*1000 + self.unique_time.minute*60*1000 + self.unique_time.second*1000 + self.unique_time.microsecond*1000
        stop = self.stop_time.hour*60*60*1000 + self.stop_time.minute*60*1000 + self.stop_time.second*1000 + self.stop_time.microsecond*1000
        milli_diff = (stop - unique)
        sandwich_num = max(0, (milli_diff - ((60*6 + 12)*60*1000))/(1000*60*30))
        self.sandwiches = math.ceil(sandwich_num)


    def __unicode__(self):
        return self.establishment
