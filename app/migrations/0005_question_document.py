# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='document',
            field=models.ForeignKey(to='app.Document', null=True),
            preserve_default=True,
        ),
    ]
