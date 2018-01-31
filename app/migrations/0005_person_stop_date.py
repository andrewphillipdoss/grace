# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20180119_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='stop_date',
            field=models.DateField(default=datetime.date(2018, 1, 31)),
        ),
    ]
