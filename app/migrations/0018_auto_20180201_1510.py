# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20180201_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='unique_date',
            field=models.DateField(),
        ),
    ]
