# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20141122_1454'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blacklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('url', models.CharField(max_length=255)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='canliidocument',
            name='databaseId',
            field=models.CharField(max_length=64, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='canliidocument',
            name='documentId',
            field=models.CharField(max_length=64, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='canliidocument',
            name='populated',
            field=models.BooleanField(db_index=True, default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='canliidocument',
            name='title',
            field=models.TextField(db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='canliidocument',
            name='type',
            field=models.IntegerField(db_index=True),
            preserve_default=True,
        ),
    ]
