# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20141110_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canliidocument',
            name='title',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
