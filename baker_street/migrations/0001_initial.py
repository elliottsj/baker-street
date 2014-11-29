# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', default=False, verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(verbose_name='email address', max_length=75, unique=True)),
                ('is_staff', models.BooleanField(help_text='Designates whether the user can log into this admin site.', default=False, verbose_name='staff status')),
                ('is_active', models.BooleanField(help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', default=True, verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, to='auth.Group', verbose_name='groups', related_query_name='user', help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', related_name='user_set')),
                ('user_permissions', models.ManyToManyField(blank=True, to='auth.Permission', verbose_name='user permissions', related_query_name='user', help_text='Specific permissions for this user.', related_name='user_set')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CanLIIDocument',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.TextField()),
                ('documentId', models.CharField(max_length=64)),
                ('databaseId', models.CharField(max_length=64)),
                ('type', models.IntegerField(db_index=True)),
                ('populated', models.BooleanField(default=False)),
                ('url', models.CharField(blank=True, max_length=255)),
                ('content', models.TextField(blank=True)),
                ('repealed', models.NullBooleanField(default=None)),
                ('citation', models.CharField(max_length=255, db_index=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Context',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('value', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('publish_date', models.DateField(null=True)),
                ('url', models.CharField(max_length=255)),
                ('pinned', models.BooleanField(default=False)),
                ('content', models.TextField()),
                ('type', models.IntegerField()),
                ('source', models.CharField(max_length=255, default='CanLII')),
                ('canlii', models.ForeignKey(to='baker_street.CanLIIDocument')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Evidence',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
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
            name='InviteCode',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('code', models.CharField(max_length=16, default='')),
                ('used', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('page_url', models.TextField()),
                ('title', models.TextField(blank=True)),
                ('content', models.TextField(blank=True)),
                ('most_recent', models.BooleanField(default=False)),
                ('snippet', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('question_text', models.TextField()),
                ('document', models.ForeignKey(to='baker_street.Document', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResearchSession',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('current', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sitelist',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VectorSet',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('word', models.CharField(max_length=255, db_index=True)),
                ('weight', models.IntegerField()),
                ('session', models.ForeignKey(to='baker_street.ResearchSession')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('url', models.CharField(max_length=255, default='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='sitelist',
            name='websites',
            field=models.ManyToManyField(to='baker_street.Website'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='researchsession',
            name='sitelist',
            field=models.OneToOneField(to='baker_street.Sitelist'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='researchsession',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='page',
            name='research_session',
            field=models.ForeignKey(to='baker_street.ResearchSession'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='document',
            name='page',
            field=models.ForeignKey(to='baker_street.Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='document',
            name='session',
            field=models.ForeignKey(to='baker_street.ResearchSession'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='context',
            name='research_session',
            field=models.ForeignKey(to='baker_street.ResearchSession'),
            preserve_default=True,
        ),
    ]
