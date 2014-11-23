# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baker_street', '0005_auto_20141122_0326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='id',
        ),
        migrations.AddField(
            model_name='document',
            name='canlii',
            field=models.OneToOneField(primary_key=True, to='baker_street.CanLIIDocument', serialize=False, default=0),
            preserve_default=False,
        ),
    ]
