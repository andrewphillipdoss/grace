# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_person_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='stop_time',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='unique_time',
            field=models.TimeField(null=True, blank=True),
        ),
    ]
