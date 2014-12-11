# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_add_project_img_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='video',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
