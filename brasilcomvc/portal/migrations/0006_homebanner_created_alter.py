# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_homebanner_verbose'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homebanner',
            name='created',
            field=models.DateTimeField(editable=False, default=django.utils.timezone.now),
            preserve_default=True,
        ),
    ]
