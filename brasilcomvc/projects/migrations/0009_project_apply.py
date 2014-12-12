# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0008_project_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectApply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(editable=False, to='projects.Project', related_name='applications')),
                ('volunteer', models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL, related_name='applications')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='projectapply',
            unique_together=set([('project', 'volunteer')]),
        ),
    ]
