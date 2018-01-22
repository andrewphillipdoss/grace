from django.db import models

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

    def __unicode__(self):
        return self.establishment
