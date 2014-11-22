# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20141122_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='content',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='source',
            field=models.CharField(max_length=255, default='CanLII'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='document',
            name='type',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
