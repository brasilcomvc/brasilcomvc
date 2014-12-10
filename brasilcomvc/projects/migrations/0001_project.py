# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('relevant_fact', models.TextField(blank=True, null=True)),
                ('about', models.TextField()),
                ('short_description', models.TextField(blank=True, null=True)),
                ('how_to_help', models.TextField()),
                ('requirements', models.TextField()),
                ('owner', models.ForeignKey(related_name='projects_owned', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
