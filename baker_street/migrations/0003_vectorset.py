# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_populate_canlii'),
    ]

    operations = [
        migrations.CreateModel(
            name='VectorSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('word', models.CharField(max_length=255)),
                ('weight', models.IntegerField()),
                ('session', models.ForeignKey(to='api.ResearchSession')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
