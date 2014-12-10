# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields
import brasilcomvc.projects.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_add_project_verbose_names'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='img',
            field=imagekit.models.fields.ProcessedImageField(default='', upload_to=brasilcomvc.projects.models.project_img_upload_to),
            preserve_default=False,
        ),
    ]
