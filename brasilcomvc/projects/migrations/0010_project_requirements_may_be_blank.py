# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_project_apply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='requirements',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
