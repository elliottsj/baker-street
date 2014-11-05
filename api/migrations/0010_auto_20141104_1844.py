# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_document_session'),
    ]

    operations = [
        migrations.AddField(
            model_name='researchsession',
            name='current',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
