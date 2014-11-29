# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import baker_street.models


class Migration(migrations.Migration):

    dependencies = [
        ('baker_street', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitecode',
            name='code',
            field=models.CharField(max_length=16, default=baker_street.models._get_new),
            preserve_default=True,
        ),
    ]
