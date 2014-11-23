# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_enumfield.db.fields
import django.utils.timezone
import django_enumfield.enum
from django.conf import settings
import baker_street.enums


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(max_length=30, blank=True, verbose_name='first name')),
                ('last_name', models.CharField(max_length=30, blank=True, verbose_name='last name')),
                ('email', models.EmailField(max_length=75, unique=True, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(to='auth.Group', help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', related_query_name='user', related_name='user_set', verbose_name='groups', blank=True)),
                ('user_permissions', models.ManyToManyField(to='auth.Permission', help_text='Specific permissions for this user.', related_query_name='user', related_name='user_set', verbose_name='user permissions', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Blacklist',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CanLIIDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.TextField()),
                ('documentId', models.CharField(max_length=64)),
                ('databaseId', models.CharField(max_length=64)),
                ('type', models.IntegerField(db_index=True)),
                ('populated', models.BooleanField(default=False)),
                ('url', models.CharField(max_length=255, blank=True)),
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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('value', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('publish_date', models.DateField(null=True)),
                ('url', models.CharField(max_length=255)),
                ('pinned', models.BooleanField(default=False)),
                ('content', models.TextField()),
                ('type', models.IntegerField()),
                ('source', models.CharField(max_length=255, default='CanLII')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Evidence',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('page_url', models.TextField()),
                ('title', models.TextField(blank=True)),
                ('content', models.TextField(blank=True)),
                ('website', django_enumfield.db.fields.EnumField(default=0, enum=baker_street.enums.Website, choices=[(0, django_enumfield.enum.Value('NONE', 0, 'NONE', baker_street.enums.Website)), (1, django_enumfield.enum.Value('CANLII', 1, 'CANLII', baker_street.enums.Website))])),
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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('question_text', models.TextField()),
                ('document', models.ForeignKey(null=True, to='baker_street.Document')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResearchSession',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('current', models.BooleanField(default=False)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='page',
            name='research_session',
            field=models.ForeignKey(to='baker_street.ResearchSession'),
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
