# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20180131_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='unique_date',
            field=models.DateField(default=datetime.datetime(2018, 1, 31, 22, 26, 39, 912887, tzinfo=utc)),
        ),
    ]
