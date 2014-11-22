# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_auto_20141122_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canliidocument',
            name='citation',
            field=models.CharField(max_length=255, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='canliidocument',
            name='databaseId',
            field=models.CharField(max_length=64),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='canliidocument',
            name='documentId',
            field=models.CharField(max_length=64),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='canliidocument',
            name='populated',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='canliidocument',
            name='title',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
