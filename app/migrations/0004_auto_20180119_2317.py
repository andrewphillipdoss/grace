# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20180119_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='sandwiches',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
