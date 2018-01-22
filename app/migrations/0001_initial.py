# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('type_person', models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])),
                ('label', models.CharField(max_length=30)),
                ('eligible', models.BooleanField()),
                ('unique_time', models.TimeField(blank=True)),
                ('sandwiches', models.PositiveSmallIntegerField()),
                ('stop_time', models.TimeField(blank=True)),
            ],
        ),
    ]
