# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20141103_2155'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='url',
            new_name='page_url',
        ),
        migrations.RemoveField(
            model_name='researchsession',
            name='name',
        ),
    ]
