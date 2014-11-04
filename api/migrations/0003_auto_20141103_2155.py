# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_enumfield.db.fields
import django_enumfield.enum
import api.enums


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20141104_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='website',
            field=django_enumfield.db.fields.EnumField(default=0, enum=api.enums.Website, choices=[(0, django_enumfield.enum.Value('NONE', 0, 'NONE', api.enums.Website)), (1, django_enumfield.enum.Value('CANLII', 1, 'CANLII', api.enums.Website))]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='content',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
