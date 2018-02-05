# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20180201_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='unique_date',
            field=models.DateField(default=datetime.datetime(2018, 2, 1, 21, 9, 53, 519, tzinfo=utc)),
        ),
    ]
