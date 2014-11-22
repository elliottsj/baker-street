# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baker_street', '0004_document_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vectorset',
            name='word',
            field=models.CharField(max_length=255, db_index=True),
            preserve_default=True,
        ),
    ]
