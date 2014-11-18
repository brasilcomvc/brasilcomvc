# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.SlugField(max_length=30, blank=True, null=True),
            preserve_default=True,
        ),
    ]
