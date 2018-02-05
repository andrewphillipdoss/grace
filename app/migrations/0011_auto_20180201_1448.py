# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20180201_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='unique_date',
            field=models.DateField(default=datetime.datetime(2018, 2, 1, 20, 48, 55, 655095, tzinfo=utc)),
        ),
    ]
