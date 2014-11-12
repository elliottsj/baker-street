# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_canliidocument_watson_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='canliidocument',
            name='watson_title',
        ),
        migrations.AddField(
            model_name='canliidocument',
            name='populated',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='canliidocument',
            name='type',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='canliidocument',
            name='content',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='canliidocument',
            name='url',
            field=models.CharField(blank=True, max_length=255),
            preserve_default=True,
        ),
    ]
