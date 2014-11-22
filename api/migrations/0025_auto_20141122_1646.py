# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_auto_20141122_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='snippet',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
