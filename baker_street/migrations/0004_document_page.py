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
            field=models.ForeignKey(default=1, to='baker_street.Page'),
            preserve_default=False,
        ),
    ]
