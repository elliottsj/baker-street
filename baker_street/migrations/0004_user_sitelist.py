# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baker_street', '0003_sitelist'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='sitelist',
            field=models.OneToOneField(default=0, to='baker_street.Sitelist'),
            preserve_default=False,
        ),
    ]
