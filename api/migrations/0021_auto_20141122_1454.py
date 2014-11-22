# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_auto_20141122_1349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prioritizedtext',
            name='research_session',
        ),
        migrations.DeleteModel(
            name='PrioritizedText',
        ),
        migrations.AddField(
            model_name='page',
            name='snippet',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
