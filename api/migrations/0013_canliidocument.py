# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_page_most_recent'),
    ]

    operations = [
        migrations.CreateModel(
            name='CanLIIDocument',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('documentId', models.CharField(max_length=64)),
                ('databaseId', models.CharField(max_length=64)),
                ('url', models.CharField(max_length=64)),
                ('content', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
