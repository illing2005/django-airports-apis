# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('iata', models.CharField(max_length=3, null=True, blank=True)),
                ('icao', models.CharField(max_length=4, null=True, blank=True)),
                ('name', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('country_code', models.CharField(max_length=10, null=True, blank=True)),
                ('time_zone', models.CharField(max_length=255, null=True, blank=True)),
                ('longitude', models.CharField(max_length=255, null=True, blank=True)),
                ('latitude', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
