# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('omms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sightinfo',
            name='corrected_sight',
            field=models.CharField(verbose_name='矫正视力', max_length=45),
        ),
    ]
