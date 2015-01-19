# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_homebanner'),
    ]

    operations = [
        migrations.AddField(
            model_name='homebanner',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 19, 14, 17, 46, 357346, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
