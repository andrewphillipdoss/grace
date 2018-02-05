# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20180201_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='unique_date',
            field=models.DateField(default=datetime.datetime(2018, 2, 1, 21, 7, 45, 300331, tzinfo=utc)),
        ),
    ]
