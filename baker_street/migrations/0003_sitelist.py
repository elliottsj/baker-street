# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baker_street', '0002_whitelist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sitelist',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('url', models.CharField(default='', max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='blacklist',
            name='user',
        ),
        migrations.DeleteModel(
            name='Blacklist',
        ),
        migrations.RemoveField(
            model_name='whitelist',
            name='user',
        ),
        migrations.DeleteModel(
            name='Whitelist',
        ),
        migrations.AddField(
            model_name='sitelist',
            name='websites',
            field=models.ManyToManyField(to='baker_street.Website'),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='page',
            name='website',
        ),
        migrations.AddField(
            model_name='researchsession',
            name='sitelist',
            field=models.OneToOneField(default=0, to='baker_street.Sitelist'),
            preserve_default=False,
        ),
    ]
