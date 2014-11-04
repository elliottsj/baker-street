# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20141103_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='pinned',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
