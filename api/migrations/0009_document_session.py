# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20141104_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='session',
            field=models.ForeignKey(default=1, to='api.ResearchSession'),
            preserve_default=False,
        ),
    ]
