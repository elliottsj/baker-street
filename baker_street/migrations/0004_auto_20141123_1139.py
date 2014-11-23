# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baker_street', '0003_vectorset'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='page',
            field=models.ForeignKey(default=None, to='baker_street.Page'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vectorset',
            name='word',
            field=models.CharField(db_index=True, max_length=255),
            preserve_default=True,
        ),
    ]
