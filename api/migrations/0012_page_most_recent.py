# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20141104_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='most_recent',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
