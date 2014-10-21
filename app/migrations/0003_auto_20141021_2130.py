# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20141021_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='publish_date',
            field=models.DateField(null=True),
        ),
    ]
