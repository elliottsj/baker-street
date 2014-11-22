# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_auto_20141122_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='canliidocument',
            name='citation',
            field=models.CharField(max_length=255, default=''),
            preserve_default=False,
        ),
    ]
