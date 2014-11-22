# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20141111_2359'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrioritizedText',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('research_session', models.ForeignKey(to='api.ResearchSession')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='canliidocument',
            name='repealed',
            field=models.NullBooleanField(default=None),
            preserve_default=True,
        ),
    ]
