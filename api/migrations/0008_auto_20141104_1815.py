# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20141104_1719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='pinned',
        ),
        migrations.AddField(
            model_name='document',
            name='pinned',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='document',
            name='url',
            field=models.CharField(max_length=255, default=''),
            preserve_default=False,
        ),
    ]
