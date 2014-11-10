# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_canliidocument'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canliidocument',
            name='title',
            field=models.TextField(max_length=255),
            preserve_default=True,
        ),
    ]
