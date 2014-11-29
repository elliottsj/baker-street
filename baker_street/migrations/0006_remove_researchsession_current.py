# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baker_street', '0005_remove_user_sitelist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='researchsession',
            name='current',
        ),
    ]
