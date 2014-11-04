# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_page_pinned'),
    ]

    operations = [
        migrations.AddField(
            model_name='researchsession',
            name='name',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
    ]
