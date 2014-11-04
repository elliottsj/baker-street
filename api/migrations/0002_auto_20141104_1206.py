# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Context',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('value', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Evidence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('copyright', models.CharField(max_length=255)),
                ('external_id', models.CharField(max_length=255)),
                ('terms_of_use', models.CharField(max_length=255)),
                ('document_path', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('confidence', models.FloatField()),
                ('original_file', models.CharField(max_length=255)),
                ('deepqa_id', models.CharField(max_length=255)),
                ('corpus_name', models.CharField(max_length=255)),
                ('docno', models.CharField(max_length=255)),
                ('corpus_plus_docno', models.CharField(max_length=255)),
                ('file_name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('url', models.TextField()),
                ('title', models.TextField()),
                ('content', models.TextField()),
                ('document', models.OneToOneField(to='api.Document')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResearchSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='page',
            name='research_session',
            field=models.ForeignKey(to='api.ResearchSession'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='page',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='context',
            name='research_session',
            field=models.ForeignKey(to='api.ResearchSession'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='document',
            name='title',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
    ]
