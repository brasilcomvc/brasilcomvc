# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import brasilcomvc.portal.models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_homebanner_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='homebanner',
            name='video',
            field=models.FileField(null=True, help_text='Vídeo curto e leve; ficará em loop.', blank=True, upload_to=brasilcomvc.portal.models.homebanner_video_upload_to),
            preserve_default=True,
        ),
    ]
