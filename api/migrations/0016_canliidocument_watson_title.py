# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20141110_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='canliidocument',
            name='watson_title',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
